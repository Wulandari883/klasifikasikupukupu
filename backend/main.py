import json
from pathlib import Path

import uvicorn
import numpy as np
import tensorflow as tf

from PIL import Image

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware


# ============================================================
# PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DEPLOY_DIR = (
    BASE_DIR
    / "model"
    / "butterfly_sobel_deployment_v3"
)

SAVED_MODEL_PATH = (
    DEPLOY_DIR
    / "butterfly_sobel_savedmodel_v3"
)

CONFIG_PATH = (
    DEPLOY_DIR
    / "butterfly_sobel_50class_ood_config_v3.json"
)

PROTOTYPE_PATH = (
    DEPLOY_DIR
    / "butterfly_sobel_50class_prototypes_v3.npy"
)


# ============================================================
# FASTAPI
# ============================================================

app = FastAPI(
    title="Butterfly Classification API",
    description=(
        "Butterfly Species Classification "
        "using EfficientNetB0 + Sobel Edge Detection "
        "+ OOD Rejection"
    ),
    version="3.0.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# CEK FILE MODEL
# ============================================================

print("==========================================")
print("CHECKING MODEL FILES")
print("==========================================")

print("SavedModel :", SAVED_MODEL_PATH)
print("Config     :", CONFIG_PATH)
print("Prototype  :", PROTOTYPE_PATH)

if not SAVED_MODEL_PATH.exists():
    raise FileNotFoundError(
        f"SavedModel tidak ditemukan:\n{SAVED_MODEL_PATH}"
    )

if not CONFIG_PATH.exists():
    raise FileNotFoundError(
        f"Config tidak ditemukan:\n{CONFIG_PATH}"
    )

if not PROTOTYPE_PATH.exists():
    raise FileNotFoundError(
        f"Prototype tidak ditemukan:\n{PROTOTYPE_PATH}"
    )

print("Semua file model ditemukan!")


# ============================================================
# LOAD CONFIG
# ============================================================

print()
print("Loading OOD configuration...")

with open(
    CONFIG_PATH,
    "r",
    encoding="utf-8"
) as f:

    CONFIG = json.load(f)


CLASS_NAMES = CONFIG["class_names"]

NUM_CLASSES = int(
    CONFIG["num_classes"]
)

CONFIDENCE_THRESHOLD = float(
    CONFIG["confidence_threshold"]
)

SIMILARITY_THRESHOLD = float(
    CONFIG["similarity_threshold"]
)


print("Jumlah kelas:", NUM_CLASSES)

print(
    "Confidence threshold:",
    CONFIDENCE_THRESHOLD
)

print(
    "Similarity threshold:",
    SIMILARITY_THRESHOLD
)


# ============================================================
# LOAD PROTOTYPE
# ============================================================

print()
print("Loading OOD prototypes...")

PROTOTYPES = np.load(
    PROTOTYPE_PATH
)

print(
    "Prototype shape:",
    PROTOTYPES.shape
)


# ============================================================
# NORMALIZE PROTOTYPES
# ============================================================

def normalize_vectors(
    vectors
):

    norms = np.linalg.norm(
        vectors,
        axis=1,
        keepdims=True
    )

    return vectors / (
        norms + 1e-8
    )


PROTOTYPES = normalize_vectors(
    PROTOTYPES
)


# ============================================================
# VALIDASI JUMLAH KELAS
# ============================================================

if len(CLASS_NAMES) != NUM_CLASSES:

    raise ValueError(
        "Jumlah CLASS_NAMES tidak sesuai "
        "dengan NUM_CLASSES!"
    )


if PROTOTYPES.shape[0] != NUM_CLASSES:

    raise ValueError(
        "Jumlah prototype tidak sesuai "
        "dengan jumlah kelas!"
    )


print(
    "Jumlah class dan prototype sesuai."
)


# ============================================================
# LOAD SAVEDMODEL
# ============================================================

print()
print("==========================================")
print("LOADING SAVEDMODEL")
print("==========================================")

model = tf.saved_model.load(
    str(SAVED_MODEL_PATH)
)

print(
    "SavedModel berhasil dimuat."
)


# ============================================================
# SIGNATURE
# ============================================================

print()
print(
    "Available signatures:",
    list(model.signatures.keys())
)


if "serve" in model.signatures:

    infer = model.signatures["serve"]

elif "serving_default" in model.signatures:

    infer = model.signatures[
        "serving_default"
    ]

else:

    raise RuntimeError(
        "Signature 'serve' atau "
        "'serving_default' tidak ditemukan."
    )


print()
print("INPUT MODEL:")
print(
    infer.structured_input_signature
)

print()
print("OUTPUT MODEL:")
print(
    infer.structured_outputs
)

print()
print(
    "Model EfficientNetB0 + Sobel "
    "berhasil dimuat!"
)


# ============================================================
# NORMALIZE EMBEDDING
# ============================================================

def normalize_embedding(
    embedding
):

    embedding = np.asarray(
        embedding,
        dtype=np.float32
    )

    norm = np.linalg.norm(
        embedding,
        axis=1,
        keepdims=True
    )

    return embedding / (
        norm + 1e-8
    )


# ============================================================
# OOD / REJECTION
# ============================================================

def calculate_similarity(
    embedding
):

    """
    Menghitung cosine similarity
    embedding gambar terhadap prototype
    50 kelas.
    """

    embedding = normalize_embedding(
        embedding
    )

    similarities = np.matmul(
        embedding,
        PROTOTYPES.T
    )

    max_similarity = np.max(
        similarities,
        axis=1
    )

    return max_similarity


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/api/health")
def health_check():

    return {
        "status": "healthy",
        "model": (
            "EfficientNetB0 + "
            "Sobel Edge Detection + "
            "OOD Rejection"
        ),
        "classes": NUM_CLASSES
    }


# ============================================================
# PREDICT
# ============================================================

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    try:

        # ====================================================
        # 1. BACA GAMBAR
        # ====================================================

        image = Image.open(
            file.file
        ).convert("RGB")


        # ====================================================
        # 2. RESIZE
        # ====================================================

        image = image.resize(
            (224, 224)
        )


        # ====================================================
        # 3. NUMPY
        # ====================================================

        image = np.array(
            image,
            dtype=np.float32
        )


        # ====================================================
        # 4. BATCH DIMENSION
        # ====================================================

        image = np.expand_dims(
            image,
            axis=0
        )


        # ====================================================
        # PENTING
        # ====================================================
        #
        # JANGAN gunakan:
        #
        # tf.keras.applications.efficientnet.preprocess_input()
        #
        # karena preprocessing + Sobel + fusion
        # sudah menjadi bagian dari model yang
        # kita training.
        #
        # Input dikirim dalam range 0-255.
        # ====================================================


        input_tensor = tf.constant(
            image,
            dtype=tf.float32
        )


        # ====================================================
        # 5. PREDIKSI MODEL
        # ====================================================

        result = infer(
            input_layer=input_tensor
        )


        # ====================================================
        # 6. AMBIL CLASSIFIER
        # ====================================================

        if "classifier" in result:

            prediction = (
                result["classifier"]
                .numpy()
            )

        else:

            # fallback jika nama output berbeda
            output_values = list(
                result.values()
            )

            prediction = (
                output_values[0]
                .numpy()
            )


        # ====================================================
        # 7. AMBIL EMBEDDING
        # ====================================================

        if "embedding" in result:

            embedding = (
                result["embedding"]
                .numpy()
            )

        else:

            # Cari output dengan dimensi 1280
            embedding = None

            for value in result.values():

                array = value.numpy()

                if (
                    len(array.shape) == 2
                    and
                    array.shape[1] == 1280
                ):

                    embedding = array

                    break

            if embedding is None:

                raise RuntimeError(
                    "Output embedding tidak ditemukan "
                    "di SavedModel."
                )


        # ====================================================
        # 8. AMBIL CLASS TERBAIK
        # ====================================================

        prediction = prediction[0]

        class_index = int(
            np.argmax(prediction)
        )


        # ====================================================
        # 9. CONFIDENCE
        # ====================================================

        confidence = float(
            np.max(prediction)
        )


        # ====================================================
        # 10. OOD SIMILARITY
        # ====================================================

        similarity = float(
            calculate_similarity(
                embedding
            )[0]
        )


        # ====================================================
        # DEBUG
        # ====================================================

        print()
        print("========== PREDICTION ==========")

        print(
            "Class index:",
            class_index
        )

        print(
            "Class:",
            CLASS_NAMES[class_index]
        )

        print(
            "Confidence:",
            confidence
        )

        print(
            "Similarity:",
            similarity
        )

        print(
            "Confidence threshold:",
            CONFIDENCE_THRESHOLD
        )

        print(
            "Similarity threshold:",
            SIMILARITY_THRESHOLD
        )


        # ====================================================
        # 11. REJECTION
        # ====================================================

        is_valid = (

            confidence
            >= CONFIDENCE_THRESHOLD

            and

            similarity
            >= SIMILARITY_THRESHOLD

        )


        # ====================================================
        # 12. KALAU TIDAK TERDETEKSI
        # ====================================================

        if not is_valid:

            print(
                "RESULT: TIDAK TERDETEKSI"
            )

            # PENTING:
            # Tidak mengirim confidence.

            return {
                "species": "Tidak terdeteksi"
            }


        # ====================================================
        # 13. KALAU VALID
        # ====================================================

        species = CLASS_NAMES[
            class_index
        ]

        confidence_percent = (
            confidence * 100
        )


        print(
            "RESULT:",
            species
        )

        print(
            "================================"
        )


        # ====================================================
        # 14. RESPONSE
        # ====================================================

        return {

            "species": species,

            "confidence": round(
                confidence_percent,
                2
            )

        }


    # ========================================================
    # ERROR
    # ========================================================

    except Exception as e:

        print()
        print(
            "Prediction error:",
            str(e)
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ============================================================
# RUN SERVER
# ============================================================

if __name__ == "__main__":

    uvicorn.run(

        "main:app",

        host="127.0.0.1",

        port=8000,

        reload=True

    )