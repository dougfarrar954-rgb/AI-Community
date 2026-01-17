# Listening Test Prompts

> **Note for Antigravity Agent**: Since you cannot hear audio, these tests focus on **code analysis**, **waveform visualization**, and **student descriptions** of what they hear. Guide students to connect code to sound through prediction and verification.

## How to Use These Tests

### For Students:
1. Run the script and listen to the output
2. Describe what you hear in technical terms
3. Predict what code changes would alter the sound
4. Verify your predictions by modifying the code

### For Antigravity Agent:
1. Ask students to **describe** what they hear
2. Guide them to **visualize** waveforms using matplotlib
3. Have them **predict** how code changes affect sound
4. Help them **analyze** the relationship between code and audio output

---

## Module 0: Python Foundations

*No listening tests - this module focuses on pure Python syntax*

---

## Module 2: Waveforms

### Test 2.1: Waveform Identification
**Instructions**: Listen to four different waveforms at 440Hz.

**Questions**:
1. Which one sounds the smoothest? (Sine)
2. Which one sounds the "buzziest" or most "harsh"? (Square)
3. Which one sounds like it's "ramping" up and down? (Sawtooth)
4. Which one sounds between sine and square? (Triangle)

### Test 2.2: Harmonic Content
**Instructions**: Compare a sine wave to a square wave at the same frequency.

**Questions**:
1. The square wave sounds "richer" - why?
2. What makes it sound different if they're both at 440Hz?

**Expected Understanding**: Square waves contain odd harmonics, making them sound fuller than pure sine waves.

---

## Module 3: Envelopes

### Test 3.1: ADSR Recognition
**Instructions**: Listen to three synthesized sounds with different ADSR settings.

**Sound A**: Fast attack, no sustain, short release (percussive)
**Sound B**: Slow attack, long sustain, long release (pad)
**Sound C**: Medium attack, short decay, no sustain (pluck)

**Questions**:
1. Which sound most resembles a drum hit?
2. Which sound most resembles a violin bow draw?
3. Which sound most resembles a guitar pluck?

**Expected Understanding**: Envelope shapes determine instrument-like characteristics.

---

## Module 4: Filters

### Test 4.1: Low-Pass vs High-Pass
**Instructions**: Listen to white noise with different filters applied.

**Questions**:
1. Which version sounds "muffled" or "darker"?
2. Which version sounds "bright" or "thin"?
3. What frequencies are being removed in each case?

**Expected Understanding**: Low-pass filters remove high frequencies, high-pass filters remove low frequencies.

---

## Module 5: Additive Synthesis

### Test 5.1: Harmonic Stacking
**Instructions**: Listen to progressively more harmonics being added to a fundamental.

**Questions**:
1. Does the sound get "richer" or "thinner" as harmonics are added?
2. Can you still hear the fundamental frequency?
3. What happens to the timbre?

---

## Module 6: Effects

### Test 6.1: Delay Recognition
**Instructions**: Compare a dry signal to one with delay effect.

**Questions**:
1. Describe what you hear happening over time.
2. How many "echoes" do you count?
3. What parameter controls the spacing between echoes?

---

## General Listening Skills

### Critical Listening Checklist
When analyzing any sound, ask yourself:
- [ ] What is the overall texture? (smooth, harsh, rough, clean)
- [ ] What frequencies dominate? (low, mid, high)
- [ ] How does it change over time? (static, evolving)
- [ ] What is the amplitude envelope shape?
- [ ] Are there rhythmic patterns?

---

## Instructor Notes

Use these listening tests to:
1. **Assess Understanding**: Can students hear what they're coding?
2. **Develop Ear Training**: Connect technical concepts to sonic results
3. **Debug by Ear**: "What should it sound like?" vs "What does it sound like?"

**Scaffolding Questions for Agent**:
- "What did you expect to hear?"
- "What did you actually hear?"
- "What code change would create the sound you're imagining?"
