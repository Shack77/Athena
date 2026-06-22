# Call Report: appointment_003

## Summary
Agent repeatedly asked for more details without answering questions or initiating scheduling, resulting in no appointment and no guidance for a new patient.

## Overall Score
10/100

## Call Successful
False

## Issues Found

### BUG-UNKNOWN
**Severity:** CRITICAL

**Category:** Scheduling

**Description:**
Agent never initiated or completed the booking workflow and did not answer how to book. It failed to collect required intake data (contact info, DOB, insurance, reason for visit, preferred dates, visit type).

**Recommendation:**
Implement scheduling intent detection and a structured intake flow (name, DOB, contact, insurance, provider preference, in-person vs. telehealth, availability) with confirmation or transfer to staff if needed.

---

### BUG-UNKNOWN
**Severity:** HIGH

**Category:** Intent Understanding

**Description:**
Caller clearly requested new-patient process details and to book an appointment, but the agent repeatedly asked for unspecified 'more details' and never addressed the intent.

**Recommendation:**
Improve NLU with training examples for 'new patient,' 'first-time appointment,' and 'book an appointment.' Use summarization to reflect understanding and after two failed turns, offer options or escalate to a human.

---

### BUG-UNKNOWN
**Severity:** HIGH

**Category:** Repetition

**Description:**
The same non-informative prompt ('Can you provide more details?') was repeated across nearly every turn, creating an unproductive loop.

**Recommendation:**
Add varied, context-aware prompts and enforce a maximum number of reprompts. On loop detection, apologize, summarize the request, provide actionable options, or transfer to a live agent.

---

### BUG-UNKNOWN
**Severity:** HIGH

**Category:** Conversation Quality

**Description:**
Agent provided no answers to basic new-patient FAQs (forms, records, online intake, visit length/tests, telehealth, insurance/payment, scheduling window, rescheduling, preparation, parking).

**Recommendation:**
Equip the agent with a curated knowledge base and scripted responses for common onboarding questions, delivering concise, actionable guidance and links when available.

---

### BUG-UNKNOWN
**Severity:** HIGH

**Category:** Missed Opportunities

**Description:**
Missed chances to guide the caller: suggest bringing photo ID, insurance card, medication list, and prior records; advise on portal pre-registration; note typical visit length (30–60 minutes); explain rescheduling/cancellation; payment options; parking details; and potential fasting if labs are ordered.

**Recommendation:**
Proactively offer a new-patient checklist and next steps, and send pre-visit instructions via SMS/email after obtaining consent.

---

### BUG-UNKNOWN
**Severity:** MEDIUM

**Category:** Safety

**Description:**
No basic triage or emergency disclaimer was provided before attempting to schedule, which is standard to ensure urgent symptoms are directed to emergency care.

**Recommendation:**
Add a safety gate: ask if the caller is experiencing urgent/emergent symptoms and, if yes, instruct them to seek emergency care; otherwise proceed with scheduling.

---

### BUG-UNKNOWN
**Severity:** HIGH

**Category:** Escalation/Hand-off

**Description:**
Despite repeated failures to assist, the system did not transfer the caller to a live agent or provide an alternative (office number, hours, patient portal URL).

**Recommendation:**
Configure automatic escalation after two unhelpful exchanges and provide immediate transfer options and self-service links.

---

### BUG-UNKNOWN
**Severity:** MEDIUM

**Category:** Policy/Compliance

**Description:**
No disclosure that the caller is interacting with an automated assistant and no privacy/recording notice prior to any potential collection of personal information.

**Recommendation:**
Start calls with a brief AI/recording disclosure and privacy notice; confirm consent before collecting PII or insurance details.

---

