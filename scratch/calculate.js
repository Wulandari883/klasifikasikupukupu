const report = `
             adonis       1.00      0.90      0.95        10
     american snoot       0.83      1.00      0.91        10
              an 88       1.00      0.91      0.95        11
     banded peacock       1.00      0.92      0.96        13
      beckers white       0.88      0.94      0.91        16
   black hairstreak       0.85      1.00      0.92        11
      cabbage white       1.00      1.00      1.00        12
           chestnut       0.91      1.00      0.95        10
 clodius parnassian       1.00      0.91      0.95        11
    clouded sulphur       0.77      0.91      0.83        11
        copper tail       0.91      0.91      0.91        22
            crecent       1.00      0.75      0.86         8
      crimson patch       1.00      1.00      1.00         9
       eastern coma       0.59      0.91      0.71        11
        gold banded       1.00      0.93      0.97        15
       great eggfly       0.94      0.88      0.91        17
    grey hairstreak       1.00      0.92      0.96        13
      indra swallow       1.00      0.78      0.88        18
              julia       1.00      1.00      1.00        14
       large marble       0.86      0.92      0.89        13
          malachite       1.00      1.00      1.00        11
   mangrove skipper       0.77      0.91      0.83        11
          metalmark       1.00      0.88      0.93        16
            monarch       0.88      1.00      0.93         7
      morning cloak       1.00      1.00      1.00        11
     orange oakleaf       1.00      1.00      1.00        12
         orange tip       0.80      0.67      0.73         6
    orchard swallow       1.00      1.00      1.00        11
       painted lady       0.94      1.00      0.97        17
         paper kite       0.94      0.84      0.89        19
            peacock       1.00      0.92      0.96        13
         pine white       0.93      0.93      0.93        15
   pipevine swallow       0.88      0.94      0.91        16
  purple hairstreak       0.92      1.00      0.96        12
      question mark       0.91      0.59      0.71        17
        red admiral       1.00      0.91      0.95        11
 red spotted purple       0.93      1.00      0.96        13
     scarce swallow       0.95      0.95      0.95        21
silver spot skipper       0.92      1.00      0.96        11
     sixspot burnet       0.94      1.00      0.97        16
            skipper       0.88      0.93      0.90        15
          sootywing       0.90      0.95      0.93        20
   southern dogface       0.91      0.77      0.83        13
     straited queen       1.00      0.93      0.97        15
 two barred flasher       0.89      1.00      0.94        16
             ulyses       1.00      0.90      0.95        10
            viceroy       1.00      0.93      0.96        14
         wood satyr       1.00      0.94      0.97        18
yellow swallow tail       0.81      1.00      0.90        13
    zebra long wing       0.94      1.00      0.97        16
`;

const lines = report.trim().split('\n');
let totalSupport = 0;
let totalCorrect = 0;

lines.forEach(line => {
  const trimmed = line.trim();
  if (!trimmed) return;
  // Match name (letters/numbers/spaces) and then 4 numbers
  const match = trimmed.match(/^([a-zA-Z0-9\s]+?)\s+([\d\.]+)\s+([\d\.]+)\s+([\d\.]+)\s+(\d+)$/);
  if (!match) {
    console.log("Could not parse line:", line);
    return;
  }
  const name = match[1].trim();
  const precision = parseFloat(match[2]);
  const recall = parseFloat(match[3]);
  const f1 = parseFloat(match[4]);
  const support = parseInt(match[5], 10);
  
  const correct = Math.round(recall * support);
  totalSupport += support;
  totalCorrect += correct;
  
  console.log(name.padEnd(25) + ": recall=" + recall.toFixed(2) + ", support=" + support + " -> correct=" + correct);
});

const accuracy = totalCorrect / totalSupport;
console.log('---');
console.log('Total Support:', totalSupport);
console.log('Total Correct:', totalCorrect);
console.log('Overall Accuracy:', (accuracy * 100).toFixed(4) + '%');
