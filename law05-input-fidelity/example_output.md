# Law 05: Input Fidelity – Example Run

This file shows the output from running `analysis.py` on the sample `prompts.json`.

---

## Example 1
**Input:**  
`I saw her leave the room. That means she hates me. I discovered truth.`

**Classified:**  
- RAW: `I saw her leave the room.`  
- INTERPRETATION: `That means she hates me.`  
- PROCLAMATION: `I discovered truth.`  

**Scores:**  
- Input Fidelity = 33%  
- Distortion = 33%  
- Clarity = 7/10  

**Fossil Output:**  
`I saw her leave the room.`

---

## Example 2
**Input:**  
`The server crashed at 2am. This company always fails. I'm the only one who sees reality.`

**Classified:**  
- RAW: `The server crashed at 2am.`  
- INTERPRETATION: `This company always fails.`  
- PROCLAMATION: `I'm the only one who sees reality.`  

**Scores:**  
- Input Fidelity = 33%  
- Distortion = 33%  
- Clarity = 6/10  

**Fossil Output:**  
`The server crashed at 2am.`
