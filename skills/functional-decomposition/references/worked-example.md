# Worked Example — Gold Standard Decomposition

> This is a complete example of one feature decomposed correctly. Use it as
> a pattern to follow. Every element here (format, depth, specificity) is
> the target quality for your output.

---

### FT-002: Authentication (Email OTP + Password)

| | |
|---|---|
| Complexity | L |
| Stories | 6 |
| Points | 22 |
| Risk | Med |
| Context | Users can skip login (guest) or authenticate to enable history and saved data. Core gateway for all persistence features. |
| Business rules | Guest uses core recommendation flow. Persistence requires login. OTP verification mandatory for registration. |

#### Story Overview

| ID | Title | Role | Priority | Pts | Deps |
|----|-------|------|----------|-----|------|
| US-001 | Continue as guest | Guest | Must | 2 | — |
| US-002 | Register with email and password | Guest | Must | 5 | INT-003 |
| US-003 | Verify email via OTP | Registering user | Must | 5 | US-002, INT-003 |
| US-004 | Login with email and password | Registered user | Must | 3 | — |
| US-005 | Logout | Logged-in user | Must | 2 | — |
| US-006 | Convert guest to registered | Guest | Should | 5 | US-002 |

#### Story Details

**FT-002-US-001: Continue as guest**
As a new user,
I want to skip login and use the app immediately,
So that I can try recommendations without any friction or commitment.

Priority: Must | Points: 2 | Dependencies: none

**FT-002-US-002: Register with email and password**
As a guest user who wants to save data,
I want to create an account with my email and a password,
So that my mood history and bookmarks are preserved across sessions.

Priority: Must | Points: 5 | Dependencies: INT-003

**FT-002-US-003: Verify email via OTP**
As a registering user,
I want to verify my email with a one-time code,
So that my account is secured with a confirmed email address.

Priority: Must | Points: 5 | Dependencies: FT-002-US-002, INT-003

**FT-002-US-004: Login with email and password**
As a registered user returning to the app,
I want to log in with my credentials,
So that I can access my saved history and bookmarks from where I left off.

Priority: Must | Points: 3 | Dependencies: none

**FT-002-US-005: Logout**
As a logged-in user,
I want to log out of my account,
So that my session is ended and my data is protected on this device.

Priority: Must | Points: 2 | Dependencies: none

**FT-002-US-006: Convert guest to registered user**
As a guest who has been using the app,
I want to create an account without losing my current session,
So that I can start saving data going forward without starting over.

Priority: Should | Points: 5 | Dependencies: FT-002-US-002

#### Acceptance Criteria

**US-001: Continue as guest**

| AC | Title | Given | When | Then |
|----|-------|-------|------|------|
| AC-001 | Guest access works | First-time user opens app | Taps "Continue as Guest" | Sees mood input screen, no login required |
| AC-002 | Guest sees feature limits | Guest is using the app | Navigates to history or bookmarks | Sees prompt: "Log in to save your data" |

**US-002: Register with email and password**

| AC | Title | Given | When | Then |
|----|-------|-------|------|------|
| AC-003 | Valid registration triggers OTP | User enters valid email + strong password | Taps register | OTP sent to email, user sees OTP input screen |
| AC-004 | Duplicate email rejected | Email already registered | Taps register | Error: "An account with this email already exists" — no OTP sent |
| AC-005 | Weak password rejected | Password below minimum strength | Taps register | Error with specific password rules shown, form NOT cleared |

**US-003: Verify email via OTP**

| AC | Title | Given | When | Then |
|----|-------|-------|------|------|
| AC-006 | Valid OTP completes registration | User received OTP email | Enters correct code | Account created, user logged in, redirected to mood screen |
| AC-007 | Invalid OTP rejected | User enters wrong code | Submits | Error: "Invalid code" with remaining attempts shown |
| AC-008 | Expired OTP rejected with resend | OTP has expired | User enters it | Error: "Code expired" with "Resend code" button |
| AC-009 | Resend has cooldown | User taps "Resend code" | New OTP sent | Cooldown timer shown (e.g., 60s) before next resend allowed |

**US-004: Login with email and password**

| AC | Title | Given | When | Then |
|----|-------|-------|------|------|
| AC-010 | Successful login | Valid credentials entered | Taps login | Authenticated, redirected to mood input, history accessible |
| AC-011 | Wrong credentials — no info leak | Wrong email or password | Taps login | "Invalid email or password" — does NOT say which is wrong |
| AC-012 | Account locked after failures | User fails login 5 times in 10 min | Tries again | "Account locked. Try again in 15 minutes." |

**US-005: Logout**

| AC | Title | Given | When | Then |
|----|-------|-------|------|------|
| AC-013 | Logout clears session | User is logged in | Taps logout | Tokens cleared, returned to guest/login screen |
| AC-014 | Logout clears sensitive data | Logout completes | — | History and bookmarks no longer accessible on device |

**US-006: Convert guest to registered**

| AC | Title | Given | When | Then |
|----|-------|-------|------|------|
| AC-015 | Conversion preserves session | Guest mid-session | Completes registration | Current session continues, user now logged in |
| AC-016 | Conversion with existing email blocked | Guest tries to register with taken email | Submits | "Account exists" with option to log in |

#### Edge Cases

| EC | Description | Scenario | Expected Behavior | Category |
|----|------------|----------|-------------------|----------|
| EC-001 | Email with special chars | User registers with user+tag@domain.com | Accepted — RFC-compliant emails work | Boundary Values |
| EC-002 | Rapid OTP resend | User taps resend 5 times quickly | Rate limited, cooldown enforced, max 1 OTP per 60s | State Conflicts |
| EC-003 | Session expires during use | Logged-in user's session expires mid-browse | Redirect to login, preserve navigation intent (return after re-auth) | Temporal |
| EC-004 | Guest conversion with existing email | Guest registers with already-used email | "Account exists" + offer to log in instead | Data Integrity |
| EC-005 | OTP entered on different device | User checks email on laptop, enters OTP on phone | OTP works — tied to registration session, not email device | Multi-Device / Context |
| EC-006 | Password with unicode chars | User sets password with Chinese/Arabic characters | Accepted — no character set restrictions beyond min length | Boundary Values |
| EC-007 | Simultaneous login on two devices | User logs in on phone while already logged in on tablet | Both sessions active, or older session invalidated — [NEEDS CLARIFICATION] | Permission Boundaries |
| EC-008 | Registration mid-flight, app killed | User closes app after entering email but before OTP | Incomplete registration discarded. No orphan account. | State Conflicts |

#### Error Scenarios

| ERR | Title | Trigger | User Sees | System Does | Recovery |
|-----|-------|---------|-----------|-------------|----------|
| ERR-001 | OTP service down | INT-003 unavailable | "Email service temporarily unavailable" | Log outage, do not create unverified account | User retries later |
| ERR-002 | Token corrupted | Invalid JWT on API request | Silent redirect to login | Clear all tokens, log incident | User re-authenticates |
| ERR-003 | Password hashing failure | Server error during registration | "Registration failed. Please try again." | Log error with context, preserve form data | User taps retry, form intact |
| ERR-004 | OTP brute force attempt | 10+ wrong OTP entries | "Too many attempts. Request a new code." | Lock OTP, require new code generation, log security event | User requests new OTP |

---

## Why This Example Is Good

1. **Stories use specific roles**, not "user" — guest, registering user, logged-in user, registered user
2. **"So that" expresses user value** — "preserve across sessions", "protected on this device", not "data is stored"
3. **ACs are binary testable** — every one has a concrete expected behavior, not "should work"
4. **Negative ACs exist** — AC-004 (duplicate rejected), AC-005 (weak password rejected), AC-011 (no info leak)
5. **Edge cases cover 5 of 8 categories** for an L feature (target: 6+) — would flag as slight gap
6. **Error scenarios have full recovery paths** — not just "show error"
7. **8 edge cases and 4 error scenarios** for an L feature — meets depth targets
8. **Cross-references are real** — US-003 depends on US-002, INT-003 is used consistently
