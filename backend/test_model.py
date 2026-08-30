import tensorflow as tf

print("STEP 1")

model = tf.saved_model.load(
    "model/butterfly_savedmodel"
)

print("STEP 2")

print(model)

print("STEP 3")