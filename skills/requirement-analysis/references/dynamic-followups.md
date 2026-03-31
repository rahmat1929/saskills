# Dynamic Follow-Up Logic Tree

> When a user's answer triggers a specific domain or technology context, inject these
> additional questions into the interview. These are not optional — they reflect real
> hidden complexity that the combination of answers reveals.
>
> **How to use:** During Phase 2, after each user answer, scan for trigger keywords.
> If matched, weave the follow-up questions naturally into the conversation — don't
> announce "I'm now triggering the payment follow-up tree." Just ask them as a
> thoughtful consultant would.

---

## Payment & Financial

**Triggers:** payment gateway, checkout, billing, subscription, invoice, wallet,
e-commerce, shopping cart, pricing, credit

Follow-up questions:
- Which payment gateway? (Midtrans, Xendit, DOKU, Stripe, manual transfer)
- One-time payment or recurring/subscription billing?
- Multi-currency support required?
- Refund and dispute flow — handled in the system or manually?
- Split payment or partial payment support?
- Invoice generation and PDF export needed?
- PCI-DSS compliance awareness confirmed?
- Payment reconciliation — automated or manual?
- Virtual account, QRIS, credit card, or all?
- What happens when payment fails mid-transaction? Retry logic?
- Is there a grace period for failed recurring payments?

---

## Mobile Application

**Triggers:** mobile app, iOS, Android, smartphone, app store

Follow-up questions:
- iOS, Android, or both?
- Native development or cross-platform (Flutter, React Native)?
- If both platforms: features identical or platform-specific differences?
- App store submission — who manages developer accounts (Apple, Google Play)?
- Push notification service — Firebase, APNs, or other?
- Deep linking required? (link opens specific screen in app)
- App update strategy — force update, soft prompt, or optional?
- Minimum OS version to support?
- Offline capability for any screens?
- Background location tracking or background data sync needed?
- Biometric authentication (fingerprint, Face ID)?

---

## Authentication & Multi-Role Systems

**Triggers:** login, role, permission, admin, user management, access control, auth

Follow-up questions:
- How many distinct roles exist in the system?
- Are roles fixed or can admins create custom roles?
- Is there hierarchy? (Super Admin > Admin > Manager > Staff)
- Row-level security needed? (User A can't see User B's data, same role)
- Session management: remember me, auto-logout, concurrent session limit?
- First-time login flow: invitation email, self-registration, or admin-created?
- Account deactivation vs deletion — what's the policy? Data retention?
- Password recovery flow — email, SMS, or both?
- Social login options? (Google, Facebook, Apple)
- API key or service account authentication for system-to-system?

---

## Real-Time Features

**Triggers:** real-time, live, instant, chat, notification push, websocket, live
update, live dashboard, live tracking

Follow-up questions:
- What is the acceptable latency? (sub-second, within 5 seconds, near-real-time)
- How many users need simultaneous real-time connection?
- What happens if the connection drops — graceful degradation or hard failure?
- Is message or event history required? For how long?
- Read receipts or delivery receipts needed?
- Is real-time needed on mobile as well, or web only?
- Presence indicators needed? (online/offline/away status)
- Will real-time data need to be persisted or is it ephemeral?

---

## Reporting & Analytics

**Triggers:** report, dashboard, analytics, export, chart, graph, KPI, metric,
business intelligence

Follow-up questions:
- Who consumes these reports — operational users, management, or executives?
- Is a BI tool (Metabase, Looker, Power BI) being used, or custom-built reports?
- What export formats needed? (PDF, Excel, CSV)
- Reports real-time or generated on schedule (daily, weekly)?
- Can users create custom reports or only fixed templates?
- What historical data range for reports?
- Reports shared externally? (emailed to clients, embedded in portal)
- Drill-down capability needed? (click a number to see detail)
- Data freshness requirement — can reports be 1 hour old, or must they be live?

---

## File & Media Management

**Triggers:** upload, file, document, image, video, attachment, storage, media

Follow-up questions:
- What file types allowed? (images, PDFs, videos, Office docs)
- Maximum file size per upload?
- Storage location: local server, AWS S3, Google Cloud Storage, or client's own?
- CDN needed for fast delivery (media-heavy content)?
- Image processing needed? (resize, compress, thumbnail generation)
- Private files (authenticated access) or public files?
- File versioning needed?
- Virus/malware scanning on uploads?
- Preview capability (view PDF/image in browser without download)?

---

## Data Migration

**Triggers:** existing data, migrate, import, old system, legacy, historical data,
transition

Follow-up questions:
- How much data needs migrating? (row counts, storage estimate)
- Source format — database, Excel, CSV, third-party system?
- One-time migration or parallel operation (old + new) during transition?
- Data quality of the source — clean, or needs transformation/cleaning?
- Who validates migrated data — client team or dev team?
- Rollback plan if migration fails?
- Acceptable migration downtime window?
- Are there data relationships/foreign keys that must be preserved?
- Historical audit trail — must it carry over or start fresh?

---

## Multi-Tenant / SaaS Architecture

**Triggers:** multiple clients, tenant, white-label, SaaS, organization, workspace,
multi-company

Follow-up questions:
- Single-tenant or multi-tenant?
- Data isolation: shared DB with tenant ID, or separate DB per tenant?
- Tenant customization — branding, feature flags, custom fields?
- Tenant onboarding — self-service signup or admin-provisioned?
- Billing per tenant — usage-based, flat rate, or feature-tiered?
- Cross-tenant reporting needed (super admin view across all tenants)?
- Tenant data export (data portability)?
- Tenant deletion — what happens to the data?

---

## Geolocation & Maps

**Triggers:** location, map, GPS, tracking, nearby, delivery, route, geocode,
address

Follow-up questions:
- Which maps provider? (Google Maps, Mapbox, OpenStreetMap, Here Maps)
- Real-time location tracking or one-time capture?
- Route optimization needed?
- Geofencing — trigger events when user enters/exits area?
- Location accuracy requirement (GPS, cell tower, IP-based)?
- Offline maps needed?
- Address autocomplete / geocoding for address input?
- Distance calculation between points?

---

## AI / Machine Learning Features

**Triggers:** AI, machine learning, ML, prediction, recommendation, NLP, chatbot,
classification, detection, generative

Follow-up questions:
- What specifically should AI do? (Don't accept "AI-powered" without specifics)
- Is this a pre-built AI service (OpenAI, Google Vision, AWS Comprehend) or custom model?
- What data does the AI need? Is it available and labeled?
- What is the acceptable accuracy/quality threshold?
- How is AI output presented to users — inline, as suggestions, or automated decisions?
- Human-in-the-loop review needed? Can users override AI decisions?
- Cost per API call if using external AI services — budgeted?
- Latency tolerance — can users wait 5-10 seconds for AI response?
- Fallback when AI service is unavailable?
- Training data privacy — can user data be sent to external APIs?

---

## E-Commerce / Marketplace

**Triggers:** marketplace, e-commerce, product catalog, cart, order, shop, seller,
buyer, inventory

Follow-up questions:
- Single-seller (own store) or multi-seller marketplace?
- Inventory management: real-time stock tracking or manual updates?
- Product variants (size, color, etc.)?
- Discount/promotion/coupon system?
- Order lifecycle: what states does an order go through?
- Return/refund/exchange policy and flow?
- Shipping integration — which providers? Rate calculation?
- Tax calculation — automatic or manual?
- Wishlist / save for later?
- Product review/rating system?

---

## Indonesian Market Specifics

**Triggers:** Indonesia, Indonesian users, Rupiah, IDR, local payment, NPWP, NIK,
KTP, BPJS, OJK, Kominfo

Follow-up questions:
- Payment methods: BCA VA, Mandiri, BNI, GoPay, OVO, DANA, QRIS, ShopeePay?
- Tax invoice (faktur pajak) generation needed?
- NPWP/NIK/KTP data handling — triggers UU PDP and potentially OJK compliance
- Bahasa Indonesia as primary or secondary language?
- Local hosting requirement? (some gov/regulated clients require data residency in ID)
- KOMINFO PSE registration awareness?
- Indonesian phone number format validation (+62)?
- WhatsApp integration for notifications? (dominant messaging platform in ID)
- Rupiah formatting (no decimal, dot as thousands separator)?

---

## Background Jobs & Automation

**Triggers:** schedule, cron, automated, batch, background, queue, worker, n8n,
Zapier, workflow automation

Follow-up questions:
- What triggers jobs — time-based (cron) or event-based?
- How long do jobs typically run? (seconds, minutes, hours)
- What happens if a job fails — retry logic, alert, manual rerun?
- Job monitoring and visibility — admins need to see job status?
- Are these idempotent? (safe to rerun without duplicate effects)
- Queue system needed? (Redis Queue, RabbitMQ, SQS)
- Job priority levels — some jobs more urgent than others?
- Dead letter queue — where do permanently failed jobs go?

---

## Notification & Communication

**Triggers:** notification, email, SMS, push notification, alert, message, announce

Follow-up questions:
- Which channels: email, SMS, push (mobile), in-app, WhatsApp?
- User notification preferences — can users choose which channels?
- Notification templates — who manages the content? Editable by admins?
- Bulk notifications — to all users or segments?
- Delivery tracking — need to know if email was opened/read?
- Transactional vs marketing notifications — different handling?
- Quiet hours — respect user timezone for non-urgent notifications?
- Notification center / inbox within the app?
