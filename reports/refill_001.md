# Call Report: refill_001

## Summary
Agent repeatedly asked for more details and never processed the lisinopril refill or escalated. No identity verification, no pharmacy confirmation, no next steps—creating risk of medication interruption.

## Overall Score
6/100

## Call Successful
False

## Issues Found

### BUG-UNKNOWN
**Severity:** CRITICAL

**Category:** Medication/Refill

**Description:**
Refill request was never processed. The agent failed to verify identity, confirm medication (Lisinopril 20 mg), dosing, quantity, remaining supply, prescriber, or pharmacy; did not create a refill ticket, give timelines, or confirm next steps.

**Recommendation:**
Implement a structured refill workflow: verify two identifiers; confirm med name/dose/route/sig/quantity/days’ supply, prescriber, last fill date, remaining pills, allergies/side effects/changes; capture preferred pharmacy or mail-order; collect contact info; submit refill request; provide confirmation and turnaround time; set SLA-based escalation.

---

### BUG-UNKNOWN
**Severity:** HIGH

**Category:** Intent Understanding

**Description:**
The patient clearly requested a blood pressure medication refill multiple times, but the agent did not recognize or act on the intent.

**Recommendation:**
Improve NLU for common intents (medication refill, pharmacy, prescriber). Use explicit confirmation prompts (e.g., “You’re requesting a refill of Lisinopril 20 mg—correct?”). If uncertainty persists after two turns, transfer to a human.

---

### BUG-UNKNOWN
**Severity:** HIGH

**Category:** Repetition

**Description:**
The agent repeated the exact phrase “Can you provide more details?” throughout the call with no variation or progression.

**Recommendation:**
Limit generic fallbacks to two attempts; vary prompts with targeted questions; acknowledge received information; auto-escalate to a live agent upon repeated failure.

---

### BUG-UNKNOWN
**Severity:** HIGH

**Category:** Conversational Quality

**Description:**
No acknowledgement of patient statements, no summarization, no empathy, and no closure or guidance.

**Recommendation:**
Adopt best-practice dialogue design: reflect understanding, summarize key details, confirm actions taken, provide clear next steps and timelines, and close the loop.

---

### BUG-UNKNOWN
**Severity:** HIGH

**Category:** Safety

**Description:**
Patient has ~1 week of antihypertensive medication left; the agent did not expedite, advise on urgent steps, or escalate—risking treatment interruption and uncontrolled blood pressure.

**Recommendation:**
Add safety rules: if supply <7 days, prioritize refill, notify clinic, consider short-term bridge per policy, and advise patient to contact pharmacy/clinic same day if at risk of running out.

---

### BUG-UNKNOWN
**Severity:** HIGH

**Category:** Policy/Compliance

**Description:**
No 2-identifier verification before handling a refill request; no audit trail; no escalation after repeated failures. Open-ended prompts elicited unnecessary PHI without purpose.

**Recommendation:**
Enforce identity verification (e.g., full name + DOB + address/phone) before accessing or acting on PHI. Adhere to minimum-necessary principle by asking targeted questions. After two failed turns, escalate to a human. Log actions for audit.

---

### BUG-UNKNOWN
**Severity:** MEDIUM

**Category:** Scheduling

**Description:**
Did not assess whether a follow-up visit or labs are required per clinic refill policy for ACE inhibitors (e.g., periodic BMP for K/Cr) or offer to schedule if due.

**Recommendation:**
Add rules to check last visit/lab dates and, if due or policy requires, offer to schedule a follow-up or lab draw while processing the refill.

---

### BUG-UNKNOWN
**Severity:** HIGH

**Category:** Missed Opportunities

**Description:**
Failed to collect pharmacy preference (pickup vs mail), contact method, insurance changes, or confirm prescriber; did not ask about side effects, adherence, or recent BP readings; no status updates offered.

**Recommendation:**
Expand intake to capture pharmacy details, delivery preference, contact info, insurance updates, and brief safety/adherence checks; offer text/email updates and expected readiness time.

---

### BUG-UNKNOWN
**Severity:** LOW

**Category:** Incorrect Information

**Description:**
No explicit incorrect statements were made; the problem was omission and non-response rather than misinformation.

**Recommendation:**
Provide clear outcome statements (e.g., request submitted, pending provider approval, expected turnaround). If unable to proceed, state the limitation and transfer.

---

### BUG-UNKNOWN
**Severity:** LOW

**Category:** Hallucinations

**Description:**
No fabricated facts or unsupported claims were given.

**Recommendation:**
Maintain current guardrails; focus improvements on intent handling, workflow execution, and escalation.

---

