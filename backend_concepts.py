"""
BACKEND ARCHITECT CHEAT SHEET — SCENARIO-FIRST EDITION

Target:
    Senior Backend Developer -> Lead Engineer -> Backend Architect

How to study this file:
    Do NOT memorize textbook definitions first.
    Imagine the scenario, identify the problem, then remember the solution.

Every concept follows this pattern:
    SCENARIO -> PROBLEM -> WHAT WE DO -> WHY -> REMEMBER -> INTERVIEW

Examples use realistic backend situations such as:
    users, assignments, orders, payments, reports, APIs and databases.

The examples are intentionally simple. Production systems require
additional design based on scale, consistency, security and business rules.
"""


# ============================================================
# 1. CORE PROGRAMMING & PYTHON
# ============================================================

# ------------------------------------------------------------
# DATA STRUCTURES
# ------------------------------------------------------------
# SCENARIO:
# Suppose our application receives 100,000 user records and we need to check
# very quickly whether a particular user ID already exists.
#
# PROBLEM:
# If we repeatedly search a list, the application may need to scan many items.
#
# WHAT WE DO:
# Choose the data structure based on the operation:
# list -> ordered collection
# set  -> fast uniqueness/membership checks
# dict -> key/value lookup
#
# WHY:
# The right data structure can dramatically improve performance and simplify
# the code.
#
# REMEMBER:
# "Choose the data structure based on what the application needs to do."


# ------------------------------------------------------------
# ITERATOR / GENERATOR
# ------------------------------------------------------------
# SCENARIO:
# Suppose our application has 10 million records to process.
# If we load all 10 million records into memory at once, the server may run
# out of memory.
#
# WHAT WE DO:
# Process records one at a time using an iterator/generator.
#
# Example:
# def read_users(users):
#     for user in users:
#         yield user
#
# WHY:
# Data is produced lazily instead of keeping the entire result in memory.
#
# REMEMBER:
# "Large data -> process little by little."


# ------------------------------------------------------------
# DECORATOR
# ------------------------------------------------------------
# SCENARIO:
# Suppose we have 100 API functions and every API needs logging.
# We don't want to write the same logging code inside all 100 functions.
#
# WHAT WE DO:
# Create a decorator that adds logging around the functions.
#
# WHY:
# Common behavior can be reused without changing each business function.
#
# COMMON USE:
# Logging, authentication, authorization, caching, timing, transactions.
#
# REMEMBER:
# "Add common behavior without copying it everywhere."


# ------------------------------------------------------------
# CONTEXT MANAGER
# ------------------------------------------------------------
# SCENARIO:
# Suppose our application opens a file or database/resource.
# An exception occurs halfway through processing.
# We still need to close/release the resource.
#
# WHAT WE DO:
# Use a context manager:
#
# with open("data.txt") as file:
#     data = file.read()
#
# WHY:
# Setup and cleanup happen safely even when an error occurs.
#
# REMEMBER:
# "If you acquire a resource, make sure it gets released."


# ------------------------------------------------------------
# EXCEPTION HANDLING
# ------------------------------------------------------------
# SCENARIO:
# Suppose a payment API calls our backend.
# The database is temporarily unavailable.
# If the exception is not handled, the API may return an uncontrolled error.
#
# WHAT WE DO:
# Catch expected exceptions, log useful context and return an appropriate
# response.
#
# WHY:
# Users should receive meaningful errors and the system should remain
# observable and predictable.
#
# REMEMBER:
# "Handle expected failures; don't hide unexpected failures."


# ------------------------------------------------------------
# TYPE HINTS
# ------------------------------------------------------------
# SCENARIO:
# Suppose 20 developers work on the same Python backend.
# One function accepts a user ID, but someone passes a dictionary by mistake.
#
# WHAT WE DO:
# Use type hints:
#
# def get_user(user_id: int) -> dict:
#     ...
#
# WHY:
# Makes contracts clearer and improves IDE/static-analysis support.
#
# REMEMBER:
# "Type hints make the expected shape of code obvious."


# ------------------------------------------------------------
# SOLID
# ------------------------------------------------------------
# SCENARIO:
# Suppose our OrderService contains payment logic, email logic,
# database logic and report generation.
# Every new requirement forces us to modify this huge class.
#
# PROBLEM:
# The code becomes tightly coupled and difficult to test/change.
#
# WHAT WE DO:
# Apply SOLID principles:
# S - Single Responsibility Principle: One class should have one clear responsibility.
# O - Open/Closed Principle: Add new behavior without constantly modifying stable code.
# L - Liskov Substitution Principle: Subtypes should remain usable where their base type is expected.
# I - Interface Segregation Principle: Avoid forcing classes to depend on methods they don't need.
# D - Dependency Inversion Principle: Depend on abstractions/contracts rather than concrete implementations.
#
# WHY:
# Easier maintenance, testing and extension.
#
# REMEMBER:
# "Keep responsibilities small and dependencies flexible."


# ------------------------------------------------------------
# COMPOSITION VS INHERITANCE
# ------------------------------------------------------------
# SCENARIO:
# Suppose we have different notification types:
# EmailNotification, SMSNotification and PushNotification.
# Later we need WhatsApp and Slack.
#
# PROBLEM:
# Deep inheritance can become difficult to maintain.
#
# WHAT WE DO:
# Often compose a service from smaller components/strategies instead.
#
# WHY:
# Behavior can be changed or combined without creating a large inheritance tree.
#
# REMEMBER:
# "Build objects from reusable pieces when inheritance becomes rigid."


# ============================================================
# 2. BACKEND ARCHITECTURE
# ============================================================

# ------------------------------------------------------------
# LAYERED ARCHITECTURE
# ------------------------------------------------------------
# SCENARIO:
# Suppose our FastAPI endpoint directly contains SQL, validation,
# business rules and email sending.
#
# PROBLEM:
# One API function becomes huge and difficult to test.
#
# WHAT WE DO:
# Separate responsibilities:
#
# API/Controller
#      ↓
# Service/Business Logic
#      ↓
# Repository/Data Access
#      ↓
# Database
#
# WHY:
# Each layer has a clear responsibility.
#
# REMEMBER:
# "API receives -> service decides -> repository stores."


# ------------------------------------------------------------
# CLEAN ARCHITECTURE
# ------------------------------------------------------------
# SCENARIO:
# Suppose our business logic currently depends directly on MySQL and FastAPI.
# Later the company wants PostgreSQL or another interface.
#
# PROBLEM:
# Business rules are tightly connected to infrastructure.
#
# WHAT WE DO:
# Keep business/domain logic independent and make infrastructure depend on
# abstractions around the business.
#
# WHY:
# Database/framework changes should not require rewriting core business rules.
#
# REMEMBER:
# "Business logic should not be married to the database/framework."


# ------------------------------------------------------------
# HEXAGONAL ARCHITECTURE
# ------------------------------------------------------------
# SCENARIO:
# Suppose an Order application can receive orders through REST today,
# but tomorrow it may also receive them through Kafka.
#
# WHAT WE DO:
# Keep the core order logic independent and connect REST/Kafka through adapters.
#
# WHY:
# External systems can change without rewriting the core business logic.
#
# REMEMBER:
# "Core business stays in the center; outside systems are adapters."


# ------------------------------------------------------------
# MONOLITH
# ------------------------------------------------------------
# SCENARIO:
# Suppose a team of 5 developers is building an internal application with
# moderate traffic.
#
# WHAT WE DO:
# Keep the application as one deployable backend.
#
# WHY:
# Simpler development, deployment, debugging and transactions.
#
# REMEMBER:
# "Simple system + small team -> monolith can be the best architecture."


# ------------------------------------------------------------
# MODULAR MONOLITH
# ------------------------------------------------------------
# SCENARIO:
# Suppose our application has Users, Assignments, Reports and Notifications.
# The company is not large enough to justify many independent services.
#
# WHAT WE DO:
# Keep one deployment but create strong internal modules:
#
# Users
# Assignments
# Reports
# Notifications
#
# WHY:
# We get clear boundaries without taking on full microservice complexity.
#
# REMEMBER:
# "One deployment does not mean one giant codebase."


# ------------------------------------------------------------
# MICROSERVICES
# ------------------------------------------------------------
# SCENARIO:
# Suppose the payment team needs to deploy payment changes independently,
# while the reporting team needs to scale reports separately.
#
# WHAT WE DO:
# Split independently deployable business services.
#
# WHY:
# Independent ownership, deployment and scaling.
#
# COST:
# Network calls, distributed transactions, observability, deployment and
# operational complexity.
#
# REMEMBER:
# "Microservices solve organizational/scaling problems but create
# distributed-system problems."


# ------------------------------------------------------------
# EVENT-DRIVEN ARCHITECTURE
# ------------------------------------------------------------
# SCENARIO:
# Suppose an order is created.
# We need payment processing, inventory update, notification and analytics.
#
# PROBLEM:
# If OrderService directly calls all four services synchronously,
# they become tightly coupled.
#
# WHAT WE DO:
# Publish:
#
# OrderCreated
#     ↓
# Payment
# Inventory
# Notification
# Analytics
#
# WHY:
# Consumers can react independently.
#
# REMEMBER:
# "Publish what happened; interested systems react."


# ------------------------------------------------------------
# CQRS
# ------------------------------------------------------------
# SCENARIO:
# Suppose our application receives 100 writes per second but 50,000 reads
# per second, and the read model is very different from the write model.
#
# WHAT WE DO:
# Separate command/write processing from query/read processing.
#
# WHY:
# Read and write workloads can be optimized independently.
#
# REMEMBER:
# "When reading and writing have very different needs, separate them."


# ------------------------------------------------------------
# EVENT SOURCING
# ------------------------------------------------------------
# SCENARIO:
# Suppose a financial application needs a complete history of every change
# to an account.
#
# WHAT WE DO:
# Store business events such as MoneyDeposited and MoneyWithdrawn as the
# authoritative history.
#
# WHY:
# We can reconstruct state and audit what happened.
#
# COST:
# Event versioning, replay, storage and operational complexity.
#
# REMEMBER:
# "Store the history of what happened, not only the final state."


# ============================================================
# 3. API DESIGN
# ============================================================

# ------------------------------------------------------------
# REST
# ------------------------------------------------------------
# SCENARIO:
# Suppose the frontend needs to retrieve a user.
#
# WHAT WE DO:
# GET /users/123
#
# To create:
# POST /users
#
# To partially update:
# PATCH /users/123
#
# WHY:
# HTTP provides a standard way for clients and backend services to communicate.
#
# REMEMBER:
# "Design APIs around resources and clear HTTP semantics."


# ------------------------------------------------------------
# PUT VS PATCH
# ------------------------------------------------------------
# SCENARIO:
# Suppose a user has 20 fields and wants to change only their phone number.
#
# WHAT WE DO:
# Usually use PATCH when the operation represents a partial modification.
#
# WHY:
# We don't need to send/replace the entire resource.
#
# REMEMBER:
# "PUT -> replacement semantics; PATCH -> partial modification."


# ------------------------------------------------------------
# HTTP STATUS CODES
# ------------------------------------------------------------
# SCENARIO:
# Suppose the client requests user 9999, but that user doesn't exist.
#
# WHAT WE DO:
# Return 404 instead of 500.
#
# Common thinking:
# 200 -> successful request
# 201 -> resource created
# 204 -> successful, no response body
# 400 -> invalid request
# 401 -> identity/authentication missing or invalid
# 403 -> authenticated but not allowed
# 404 -> resource not found
# 409 -> conflict
# 429 -> rate limit exceeded
# 500 -> unexpected server error
# 503 -> service temporarily unavailable
#
# REMEMBER:
# "Status codes communicate what happened to the client."


# ------------------------------------------------------------
# PAGINATION
# ------------------------------------------------------------
# SCENARIO:
# Suppose our users table has 5 million users.
# The frontend asks for all users in one API call.
#
# PROBLEM:
# Huge DB query, huge response, high memory and slow network.
#
# WHAT WE DO:
# Return manageable pages or cursors.
#
# Example:
# /users?page=2&page_size=50
#
# WHY:
# Limit database work and response size.
#
# REMEMBER:
# "Never make an API return millions of records by default."


# ------------------------------------------------------------
# IDEMPOTENCY
# ------------------------------------------------------------
# SCENARIO:
# Suppose a payment request reaches our server.
# Payment succeeds, but the network times out before the client receives
# the response.
# The client retries.
#
# PROBLEM:
# We might charge the customer twice.
#
# WHAT WE DO:
# Client sends an idempotency key.
# Backend stores the result associated with that key and prevents duplicate
# processing.

# Idempotency key:
# An idempotency key is a unique identifier generated by a client and sent to a server in an API request (typically via an HTTP header like Idempotency-Key)
# to ensure that the same operation is only processed once, even if the request is sent multiple times.

# WHY:
# Retries should not create unintended duplicate business operations.
#
# REMEMBER:
# "A retry should not accidentally become a second payment/order."


# ------------------------------------------------------------
# API VERSIONING
# ------------------------------------------------------------
# SCENARIO:
# Suppose 50 existing clients use our API response format.
# We need to introduce a breaking response change.
#
# WHAT WE DO:
# Introduce a new version or compatible contract.
#
# Example:
# /api/v1/orders
# /api/v2/orders
#
# WHY:
# Existing clients should not suddenly break.
#
# REMEMBER:
# "Changing a public contract requires compatibility planning."


# ------------------------------------------------------------
# RATE LIMITING
# ------------------------------------------------------------
# SCENARIO:
# Suppose our API normally receives 1,000 requests/minute.
# One client accidentally sends 100,000 requests/minute.
#
# PROBLEM:
# Database and application capacity can be exhausted.
#
# WHAT WE DO:
# Limit requests per client/user/IP/token.
#
# Common approaches:
# Fixed window
# Sliding window
# Token bucket
# Leaky bucket
#
# WHY:
# Protect capacity and prevent abuse.
#
# REMEMBER:
# "One client should not be able to consume the whole backend."


# ============================================================
# 4. RELATIONAL DATABASES
# ============================================================

# ------------------------------------------------------------
# PRIMARY KEY
# ------------------------------------------------------------
# SCENARIO:
# Suppose we have 10 million users.
# We need to uniquely identify one user.
#
# WHAT WE DO:
# Use a primary key such as user_id.
#
# WHY:
# Provides stable row identity and supports efficient lookup.
#
# REMEMBER:
# "Every important entity needs a reliable identity."


# ------------------------------------------------------------
# FOREIGN KEY
# ------------------------------------------------------------
# SCENARIO:
# Suppose every assignment belongs to a user.
# Someone tries to insert assignment.user_id = 999999,
# but that user doesn't exist.
#
# WHAT WE DO:
# Use a foreign key when appropriate.
#
# WHY:
# Database can enforce referential integrity.
#
# REMEMBER:
# "Don't allow relationships to point to data that doesn't exist."


# ------------------------------------------------------------
# NORMALIZATION
# ------------------------------------------------------------
# SCENARIO:
# Suppose we store the same customer address in 500 order rows.
# The customer changes the address.
#
# PROBLEM:
# Which rows should be updated? Duplicate data can become inconsistent.
#
# WHAT WE DO:
# Normalize stable/shared data into related tables.
#
# WHY:
# Reduce duplication and update anomalies.
#
# REMEMBER:
# "Store one fact in one appropriate place."


# ------------------------------------------------------------
# DENORMALIZATION
# ------------------------------------------------------------
# SCENARIO:
# Suppose a dashboard repeatedly joins five huge tables just to show a
# frequently requested summary.
#
# PROBLEM:
# The query is too expensive for the required latency.
#
# WHAT WE DO:
# Sometimes intentionally duplicate/precompute data.
#
# WHY:
# Faster reads can be worth additional storage/update complexity.
#
# REMEMBER:
# "Duplicate data deliberately when performance requirements justify it."


# ------------------------------------------------------------
# JOIN
# ------------------------------------------------------------
# SCENARIO:
# Suppose users and assignments are stored in separate tables.
# We need user name + assignment status in one response.
#
# WHAT WE DO:
# Use an appropriate JOIN.
#
# WHY:
# Let the database combine related data efficiently.
#
# REMEMBER:
# "Join related data in the database instead of making unnecessary
# application-level calls."


# ------------------------------------------------------------
# INDEX
# ------------------------------------------------------------
# SCENARIO:
# Suppose assignments has 10 million rows.
# Every request searches:
#
# WHERE user_id = 123
#
# Without a useful index, the database may scan a huge portion of the table.
#
# WHAT WE DO:
# Add an appropriate index after analyzing workload.
#
# WHY:
# Reduce lookup cost.
#
# TRADE-OFF:
# Indexes consume storage and make writes more expensive.
#
# REMEMBER:
# "Indexes speed reads but are not free."


# ------------------------------------------------------------
# COMPOSITE INDEX
# ------------------------------------------------------------
# SCENARIO:
# Suppose most queries are:
#
# WHERE user_id = ?
# AND status = ?
# ORDER BY created_at
#
# WHAT WE DO:
# Consider an index such as:
# (user_id, status, created_at)
#
# WHY:
# A well-designed composite index can support the actual query pattern.
#
# IMPORTANT:
# Column order matters.
#
# REMEMBER:
# "Design indexes for real query patterns, not just individual columns."


# ------------------------------------------------------------
# EXPLAIN
# ------------------------------------------------------------
# SCENARIO:
# Suppose an API became slow after the database grew from 100,000
# to 20 million rows.
#
# PROBLEM:
# We don't know whether the query is scanning too much data.
#
# WHAT WE DO:
# Run EXPLAIN/EXPLAIN ANALYZE where supported.
#
# WHY:
# See the database's execution plan and identify expensive operations.
#
# REMEMBER:
# "Don't guess why SQL is slow; inspect the execution plan."


# ------------------------------------------------------------
# N+1 QUERY
# ------------------------------------------------------------
# SCENARIO:
# Suppose we fetch 10,000 users:
#
# SELECT * FROM users;
#
# Then inside a Python loop:
#
# SELECT * FROM assignments WHERE user_id = ?;
#
# Result:
# 1 query + 10,000 assignment queries = 10,001 queries.
#
# PROBLEM:
# Thousands of database round trips can destroy performance.
#
# WHAT WE DO:
# Use JOINs, batch queries or carefully designed data fetching.
#
# REMEMBER:
# "One query became thousands."


# ------------------------------------------------------------
# CONNECTION POOL
# ------------------------------------------------------------
# SCENARIO:
# Suppose our API receives 1,000 concurrent requests.
# Opening a new database connection for every request is expensive.
#
# WHAT WE DO:
# Reuse a controlled pool of database connections.
#
# WHY:
# Connection creation is expensive and the database itself has capacity limits.
#
# REMEMBER:
# "Reuse DB connections; don't create unlimited connections."


# ============================================================
# 5. DATABASE CONCURRENCY
# ============================================================

# ------------------------------------------------------------
# TRANSACTION
# ------------------------------------------------------------
# SCENARIO:
# Suppose placing an order requires:
# 1. Create order
# 2. Reduce inventory
# 3. Create payment record
#
# If inventory update fails but order creation succeeds, data becomes
# inconsistent.
#
# WHAT WE DO:
# Group operations into a transaction where the consistency boundary
# belongs in the same database.
#
# WHY:
# Either all required operations succeed or they are rolled back.
#
# REMEMBER:
# "Related DB changes should succeed or fail together."


# ------------------------------------------------------------
# ACID
# ------------------------------------------------------------
# SCENARIO:
# Suppose we transfer ₹1,000 from Account A to Account B.
#
# We cannot allow:
# A -> money removed
# B -> money not added
#
# WHAT WE NEED:
# Atomicity     -> all-or-nothing
# Consistency   -> valid business/data state
# Isolation     -> concurrent operations don't improperly interfere
# Durability    -> committed data survives failure
#
# REMEMBER:
# "ACID protects important transactional data."


# ------------------------------------------------------------
# ISOLATION LEVELS
# ------------------------------------------------------------
# SCENARIO:
# Suppose many users update/read the same financial data concurrently.
# We need to decide how much one transaction should see from another.
#
# WHAT WE DO:
# Choose an appropriate isolation level:
# Read Uncommitted
# Read Committed
# Repeatable Read
# Serializable
#
# WHY:
# Stronger isolation can prevent more anomalies but may reduce concurrency.
#
# REMEMBER:
# "Isolation is a trade-off between consistency behavior and concurrency."


# ------------------------------------------------------------
# DIRTY READ
# ------------------------------------------------------------
# SCENARIO:
# Transaction A changes an order to PAID but hasn't committed.
# Transaction B reads PAID.
# Transaction A rolls back.
#
# PROBLEM:
# Transaction B saw data that never actually committed.
#
# REMEMBER:
# "You read someone else's uncommitted work."


# ------------------------------------------------------------
# NON-REPEATABLE READ
# ------------------------------------------------------------
# SCENARIO:
# Transaction A reads account balance = 10,000.
# Transaction B changes it to 8,000 and commits.
# Transaction A reads again and gets 8,000.
#
# PROBLEM:
# The same row changed during the transaction.
#
# REMEMBER:
# "Same row, different committed value."


# ------------------------------------------------------------
# PHANTOM READ
# ------------------------------------------------------------
# SCENARIO:
# Transaction A asks:
# SELECT orders WHERE status='PENDING'
# and gets 100 rows.
#
# Transaction B inserts another PENDING order and commits.
# Transaction A repeats the query and gets 101 rows.
#
# PROBLEM:
# New matching rows appeared.
#
# REMEMBER:
# "Same query, but new matching rows appeared."


# ------------------------------------------------------------
# OPTIMISTIC LOCKING
# ------------------------------------------------------------
# SCENARIO:
# Two admins open the same assignment.
# Both see version 3.
# Admin A saves first and changes version to 4.
# Admin B tries to save using version 3.
#
# WHAT WE DO:
# Update only if the version is still 3.
#
# Example:
# UPDATE assignments
# SET status='APPROVED', version=4
# WHERE id=10 AND version=3;
#
# WHY:
# Detect that someone else changed the record.
#
# REMEMBER:
# "I won't lock you first; I'll check whether someone changed it."


# ------------------------------------------------------------
# PESSIMISTIC LOCKING
# ------------------------------------------------------------
# SCENARIO:
# Suppose two workers must not modify the same inventory record at once.
#
# WHAT WE DO:
# Lock the row while performing the critical transaction.
#
# Example:
# SELECT * FROM inventory
# WHERE product_id=10
# FOR UPDATE;
#
# WHY:
# Prevent concurrent transactions from modifying the locked row
# until the transaction completes.
#
# REMEMBER:
# "Lock first when concurrent modification must be controlled."


# ------------------------------------------------------------
# RACE CONDITION
# ------------------------------------------------------------
# SCENARIO:
# Suppose two requests arrive at exactly the same time.
# Current stock = 1.
# Both requests read stock = 1.
# Both think they can purchase the last item.
#
# PROBLEM:
# Timing determines the result and both may succeed incorrectly.
#
# WHAT WE DO:
# Depending on the case, use transactions, locks, atomic SQL updates,
# unique constraints or idempotency.
#
# REMEMBER:
# "Concurrent timing changed the result."


# ------------------------------------------------------------
# DEADLOCK
# ------------------------------------------------------------
# SCENARIO:
# Transaction A locks User row then waits for Assignment row.
# Transaction B locks Assignment row then waits for User row.
#
# Both wait forever unless the database detects and aborts one.
#
# WHAT WE DO:
# Keep lock ordering consistent, keep transactions short, optimize indexes
# and retry safely after deadlock errors where appropriate.
#
# REMEMBER:
# "Two transactions are waiting for each other."


# ============================================================
# 6. NOSQL & DISTRIBUTED DATA
# ============================================================

# ------------------------------------------------------------
# NOSQL
# ------------------------------------------------------------
# SCENARIO:
# Suppose an application needs extremely high-scale key/value lookups and
# the access pattern is known in advance.
#
# WHAT WE DO:
# Consider a NoSQL database rather than forcing everything into relational SQL.
#
# WHY:
# Some workloads benefit from flexible schemas or distributed key/value
# access at very large scale.
#
# REMEMBER:
# "Choose the database from the workload and access pattern."


# ------------------------------------------------------------
# CAP THEOREM
# ------------------------------------------------------------
# SCENARIO:
# Suppose a database is replicated across two regions.
# The network connection between regions fails.
#
# PROBLEM:
# The system must decide how it behaves while the replicas cannot communicate.
#
# WHAT WE DO:
# Understand the consistency/availability trade-off during partition.
#
# REMEMBER:
# "When the network partitions, you cannot magically have every guarantee
# at the same time."


# ------------------------------------------------------------
# EVENTUAL CONSISTENCY
# ------------------------------------------------------------
# SCENARIO:
# Suppose a user changes their profile picture.
# The system has multiple replicas.
# One replica may show the old image for a short time.
#
# WHAT WE DO:
# Accept temporary inconsistency if the business allows it.
#
# WHY:
# Can improve availability and scalability.
#
# REMEMBER:
# "Different replicas may temporarily disagree, then converge."


# ============================================================
# 7. CACHING
# ============================================================

# ------------------------------------------------------------
# CACHE
# ------------------------------------------------------------
# SCENARIO:
# Suppose 20,000 users request the same program configuration every minute.
# The configuration rarely changes.
#
# PROBLEM:
# Querying MySQL 20,000 times is unnecessary.
#
# WHAT WE DO:
# Cache the configuration in Redis.
#
# Flow:
# API -> Redis
#       cache miss -> MySQL -> Redis
#
# WHY:
# Lower latency and lower database load.
#
# REMEMBER:
# "Don't repeatedly ask the database for the same answer."


# ------------------------------------------------------------
# CACHE-ASIDE
# ------------------------------------------------------------
# SCENARIO:
# Application receives a request.
#
# WHAT WE DO:
# 1. Check Redis.
# 2. If found, return it.
# 3. If not found, query DB.
# 4. Put result into Redis.
# 5. Return result.
#
# WHY:
# Simple and widely used application caching pattern.
#
# REMEMBER:
# "Application controls when data enters the cache."


# ------------------------------------------------------------
# TTL
# ------------------------------------------------------------
# SCENARIO:
# Suppose program configuration is cached for 30 minutes.
# After the program changes in DB, we don't want old data cached forever.
#
# WHAT WE DO:
# Give the cache entry a TTL.
#
# WHY:
# Automatically expires old data.
#
# REMEMBER:
# "Cache data should not live forever unless you deliberately want that."


# ------------------------------------------------------------
# CACHE INVALIDATION
# ------------------------------------------------------------
# SCENARIO:
# User changes their profile name in DB.
# Redis still contains the old name.
#
# PROBLEM:
# API returns stale data.
#
# WHAT WE DO:
# Invalidate/update the cache when appropriate.
#
# REMEMBER:
# "When source data changes, think about the cached copy."


# ------------------------------------------------------------
# CACHE STAMPEDE
# ------------------------------------------------------------
# SCENARIO:
# A popular cache key expires at 10:00 AM.
# 50,000 users request it at 10:00:01.
#
# PROBLEM:
# All requests miss Redis and hit MySQL together.
#
# WHAT WE DO:
# Use techniques such as locking/request coalescing, cache warming and
# jittered expiration.
#
# REMEMBER:
# "A cache failure can become a database traffic explosion."


# ============================================================
# 8. DISTRIBUTED SYSTEMS
# ============================================================

# ------------------------------------------------------------
# DISTRIBUTED SYSTEM
# ------------------------------------------------------------
# SCENARIO:
# Suppose our application has:
# API Server
# Payment Service
# Inventory Service
# Notification Service
# Database
#
# These components run on different machines.
#
# PROBLEM:
# Network calls can fail, become slow or return partial results.
#
# WHY:
# Distributed systems provide scale and separation but introduce failure modes
# that don't exist inside one process.
#
# REMEMBER:
# "In distributed systems, assume the network can fail."


# ------------------------------------------------------------
# REPLICATION
# ------------------------------------------------------------
# SCENARIO:
# Suppose our production database is the only copy.
# The machine fails.
#
# PROBLEM:
# Application may lose access to data.
#
# WHAT WE DO:
# Maintain replicas/backups depending on the requirement.
#
# WHY:
# Improve availability, durability and sometimes read scaling.
#
# REMEMBER:
# "One copy is a bigger failure risk."


# ------------------------------------------------------------
# SHARDING
# ------------------------------------------------------------
# SCENARIO:
# Suppose one database has become too large for the required workload.
# We have hundreds of millions of customers.
#
# WHAT WE DO:
# Split data across multiple database nodes using a shard key.
#
# WHY:
# Scale storage and traffic horizontally.
#
# CHALLENGE:
# Poor shard keys create hotspots and cross-shard queries become harder.
#
# REMEMBER:
# "Split the data, but choose the split carefully."


# ------------------------------------------------------------
# QUORUM
# ------------------------------------------------------------
# SCENARIO:
# Suppose data is stored on multiple replicas.
# We need enough replicas to acknowledge an operation before considering
# it successful.
#
# WHAT WE DO:
# Use an appropriate quorum policy.
#
# WHY:
# Balance consistency and availability based on the database/system design.
#
# REMEMBER:
# "How many replicas must agree before we proceed?"


# ------------------------------------------------------------
# DISTRIBUTED LOCK
# ------------------------------------------------------------
# SCENARIO:
# Suppose three application servers run the same scheduled job.
# We only want one of them to perform the job at a time.
#
# WHAT WE DO:
# Use a carefully designed distributed lock/lease.
#
# WHY:
# Coordinate work across machines.
#
# WARNING:
# Lock expiry, crashes and network partitions must be considered.
#
# REMEMBER:
# "A normal Python lock cannot coordinate different machines."


# ------------------------------------------------------------
# PARTIAL FAILURE
# ------------------------------------------------------------
# SCENARIO:
# API server is healthy.
# Database is healthy.
# Payment service is down.
#
# PROBLEM:
# Only one dependency failed, but it can affect the whole request.
#
# WHAT WE DO:
# Timeouts, retries where appropriate, circuit breakers, fallbacks and
# graceful degradation.
#
# REMEMBER:
# "One component can fail while everything else is still alive."


# ============================================================
# 9. MESSAGE QUEUES & EVENTS
# ============================================================

# ------------------------------------------------------------
# MESSAGE QUEUE
# ------------------------------------------------------------
# SCENARIO:
# Suppose a user uploads a file containing 10,000 rows.
# Processing takes 2 minutes.
#
# PROBLEM:
# Keeping the HTTP request open for 2 minutes is bad for user experience
# and backend reliability.
#
# WHAT WE DO:
# API puts a job into a queue.
#
# API -> Queue -> Worker
#
# WHY:
# Background processing and workload buffering.
#
# REMEMBER:
# "Put slow work in a queue instead of making the user wait."


# ------------------------------------------------------------
# PRODUCER / CONSUMER
# ------------------------------------------------------------
# SCENARIO:
# Report API creates report jobs.
# Several worker processes need to process them.
#
# WHAT WE DO:
# API is the producer.
# Workers are consumers.
#
# WHY:
# Producers and consumers can scale independently.
#
# REMEMBER:
# "Producer creates work; consumer performs work."


# ------------------------------------------------------------
# CONSUMER GROUP
# ------------------------------------------------------------
# SCENARIO:
# Suppose a Kafka topic has millions of events.
# One worker cannot process them fast enough.
#
# WHAT WE DO:
# Run multiple consumers in the same consumer group.
#
# WHY:
# Work can be distributed across consumers/partitions.
#
# REMEMBER:
# "More consumers can increase processing parallelism within partition limits."


# ------------------------------------------------------------
# AT-MOST-ONCE
# ------------------------------------------------------------
# SCENARIO:
# We process a message and choose not to retry after failure.
#
# RESULT:
# Message may be lost, but duplicate processing is minimized.
#
# REMEMBER:
# "Zero or one processing attempt."


# ------------------------------------------------------------
# AT-LEAST-ONCE
# ------------------------------------------------------------
# SCENARIO:
# A worker processes a payment notification but crashes before acknowledging
# the message.
# Queue sends the message again.
#
# PROBLEM:
# Consumer may process the same event twice.
#
# WHAT WE DO:
# Make processing idempotent.
#
# REMEMBER:
# "Reliable delivery can mean duplicate delivery; design for it."


# ------------------------------------------------------------
# EXACTLY-ONCE
# ------------------------------------------------------------
# SCENARIO:
# Business says "this payment must happen exactly once."
#
# PROBLEM:
# Network retries and crashes make end-to-end exactly-once behavior difficult.
#
# WHAT WE DO:
# Use the guarantees of the selected platform plus idempotency/transactions
# where required.
#
# REMEMBER:
# "Don't casually claim exactly-once across an entire distributed workflow."


# ------------------------------------------------------------
# DEAD LETTER QUEUE
# ------------------------------------------------------------
# SCENARIO:
# A message fails processing 10 times because its data is invalid.
#
# PROBLEM:
# Retrying forever wastes resources and can block useful work.
#
# WHAT WE DO:
# Move the message to a DLQ for investigation/reprocessing.
#
# REMEMBER:
# "Poison messages should not block the normal pipeline forever."


# ------------------------------------------------------------
# RETRY + EXPONENTIAL BACKOFF
# ------------------------------------------------------------
# SCENARIO:
# Our service calls an external API.
# It fails temporarily for 1 second.
#
# BAD:
# Retry 100 times immediately.
#
# GOOD:
# Retry after increasing delays, with limits and jitter when appropriate.
#
# WHY:
# Avoid making an unhealthy dependency even more unhealthy.
#
# REMEMBER:
# "Retry gently, not aggressively."


# ============================================================
# 10. AUTHENTICATION & AUTHORIZATION
# ============================================================

# ------------------------------------------------------------
# AUTHENTICATION
# ------------------------------------------------------------
# SCENARIO:
# A user enters username and password.
# Our backend needs to determine whether this person really is that user.
#
# WHAT WE DO:
# Verify identity.
#
# REMEMBER:
# "Who are you?"


# ------------------------------------------------------------
# AUTHORIZATION
# ------------------------------------------------------------
# SCENARIO:
# A user is successfully logged in.
# They try to delete another user's account.
#
# PROBLEM:
# Being logged in does not mean having permission.
#
# WHAT WE DO:
# Check roles/permissions/policies.
#
# REMEMBER:
# "Authentication = who; authorization = what you can do."


# ------------------------------------------------------------
# SESSION
# ------------------------------------------------------------
# SCENARIO:
# User logs into a web application.
# The server needs to remember that future browser requests belong to
# the authenticated user.
#
# WHAT WE DO:
# Use a secure session mechanism, commonly with cookies.
#
# REMEMBER:
# "The server maintains login state associated with the client."


# ------------------------------------------------------------
# JWT
# ------------------------------------------------------------
# SCENARIO:
# Several backend services need to verify identity/claims without asking
# a central session store for every request.
#
# WHAT WE DO:
# Use signed JWTs where appropriate.
#
# WHY:
# Services can validate token claims and signature.
#
# WARNING:
# A JWT is normally signed, not automatically encrypted.
#
# REMEMBER:
# "JWT is a token format, not a complete authentication architecture."


# ------------------------------------------------------------
# OAUTH 2.0
# ------------------------------------------------------------
# SCENARIO:
# A user wants an application to access a third-party API on their behalf
# without giving the application their password.
#
# WHAT WE DO:
# Use an OAuth authorization flow.
#
# REMEMBER:
# "Delegate access without sharing the user's password."


# ------------------------------------------------------------
# OPENID CONNECT
# ------------------------------------------------------------
# SCENARIO:
# Our company wants employees to sign in using a central identity provider.
#
# WHAT WE DO:
# Use an identity protocol such as OpenID Connect on top of OAuth 2.0.
#
# REMEMBER:
# "OAuth is authorization; OIDC adds an identity/authentication layer."


# ------------------------------------------------------------
# RBAC
# ------------------------------------------------------------
# SCENARIO:
# Our application has:
# Admin
# Manager
# User
#
# Admin can delete users.
# Manager can approve assignments.
# User can view their own data.
#
# WHAT WE DO:
# Map permissions to roles and roles to users.
#
# REMEMBER:
# "Permissions grouped by role."


# ------------------------------------------------------------
# LEAST PRIVILEGE
# ------------------------------------------------------------
# SCENARIO:
# A reporting service only needs SELECT access to a reporting database.
#
# BAD:
# Give it full admin access.
#
# GOOD:
# Give only the permissions required.
#
# WHY:
# If credentials are compromised, the damage is limited.
#
# REMEMBER:
# "Give the minimum permission needed."


# ============================================================
# 11. SECURITY
# ============================================================

# ------------------------------------------------------------
# SQL INJECTION
# ------------------------------------------------------------
# SCENARIO:
# Suppose we build SQL by concatenating user input.
#
# BAD:
# "SELECT * FROM users WHERE name = '" + user_input + "'"
#
# PROBLEM:
# Malicious input can alter the SQL statement.
#
# WHAT WE DO:
# Use parameterized queries/prepared statements.
#
# REMEMBER:
# "Never turn user input into executable SQL."


# ------------------------------------------------------------
# XSS
# ------------------------------------------------------------
# SCENARIO:
# A user submits a comment containing malicious JavaScript.
# The frontend displays it as raw HTML.
#
# PROBLEM:
# Another user's browser executes the script.
#
# WHAT WE DO:
# Proper output encoding, safe templating, CSP and appropriate sanitization.
#
# REMEMBER:
# "Untrusted content must not become executable browser code."


# ------------------------------------------------------------
# CSRF
# ------------------------------------------------------------
# SCENARIO:
# A logged-in browser automatically sends authentication cookies.
# An attacker tricks the browser into submitting an unwanted state-changing
# request.
#
# WHAT WE DO:
# Use appropriate CSRF protections such as tokens and SameSite cookie settings.
#
# REMEMBER:
# "Don't let another site trick a user's browser into performing actions."


# ------------------------------------------------------------
# CORS
# ------------------------------------------------------------
# SCENARIO:
# Angular frontend runs on one origin and API runs on another.
# Browser blocks the request because the API does not allow that origin.
#
# WHAT WE DO:
# Configure CORS correctly.
#
# REMEMBER:
# "CORS controls browser cross-origin access; it is not authentication."


# ------------------------------------------------------------
# TLS / HTTPS
# ------------------------------------------------------------
# SCENARIO:
# User sends a password over a public network.
#
# PROBLEM:
# Without encryption, traffic could be intercepted.
#
# WHAT WE DO:
# Use HTTPS/TLS.
#
# WHY:
# Protect data in transit and authenticate the server through certificates.
#
# REMEMBER:
# "Encrypt and protect network traffic."


# ------------------------------------------------------------
# SECRETS MANAGEMENT
# ------------------------------------------------------------
# SCENARIO:
# Developer stores a database password directly in Git.
#
# PROBLEM:
# Anyone with repository access may obtain production credentials.
#
# WHAT WE DO:
# Use environment/configuration plus a proper secrets manager and rotation.
#
# REMEMBER:
# "Passwords and API keys do not belong in source code."


# ============================================================
# 12. SCALABILITY
# ============================================================

# ------------------------------------------------------------
# VERTICAL SCALING
# ------------------------------------------------------------
# SCENARIO:
# One server has 4 CPU and 16 GB RAM.
# Traffic increases.
#
# WHAT WE DO:
# Move to a larger machine with more CPU/RAM.
#
# WHY:
# Simple way to increase capacity.
#
# LIMIT:
# Hardware/cost ceiling and single-node constraints.
#
# REMEMBER:
# "Make the machine bigger."


# ------------------------------------------------------------
# HORIZONTAL SCALING
# ------------------------------------------------------------
# SCENARIO:
# One API server cannot handle 50,000 requests/second.
#
# WHAT WE DO:
# Add more API instances behind a load balancer.
#
# API
#  ↓
# Load Balancer
#  ↓ ↓ ↓
# S1 S2 S3
#
# WHY:
# Distribute workload across machines.
#
# REMEMBER:
# "Make the fleet bigger."


# ------------------------------------------------------------
# STATELESS SERVICE
# ------------------------------------------------------------
# SCENARIO:
# Request 1 goes to Server A.
# Request 2 goes to Server B.
# If login/session state exists only in Server A's memory,
# Server B may not understand the request.
#
# WHAT WE DO:
# Keep shared state in appropriate external storage or use suitable token/session
# architecture.
#
# WHY:
# Any healthy instance can handle requests.
#
# REMEMBER:
# "Don't depend on one server's local memory if you want easy horizontal scaling."


# ------------------------------------------------------------
# LOAD BALANCER
# ------------------------------------------------------------
# SCENARIO:
# We have 10 backend servers.
# A client should not need to know which server handles its request.
#
# WHAT WE DO:
# Put a load balancer in front.
#
# WHY:
# Distribute traffic and perform health checks/routing.
#
# REMEMBER:
# "One public endpoint, many backend instances."


# ------------------------------------------------------------
# CDN
# ------------------------------------------------------------
# SCENARIO:
# Users in India, Europe and the US download the same large images.
# Sending every request to one origin server increases latency.
#
# WHAT WE DO:
# Cache suitable static content at edge locations using a CDN.
#
# WHY:
# Serve content closer to users and reduce origin load.
#
# REMEMBER:
# "Serve cacheable content near the user."


# ============================================================
# 13. RELIABILITY & FAULT TOLERANCE
# ============================================================

# ------------------------------------------------------------
# TIMEOUT
# ------------------------------------------------------------
# SCENARIO:
# Our API calls a payment service.
# Payment service becomes unresponsive.
#
# BAD:
# Wait forever.
#
# WHAT WE DO:
# Set a timeout.
#
# WHY:
# Free resources and allow failure handling.
#
# REMEMBER:
# "Every network call should have a sensible timeout."


# ------------------------------------------------------------
# RETRY
# ------------------------------------------------------------
# SCENARIO:
# External service returns a temporary network failure.
#
# WHAT WE DO:
# Retry a limited number of times with backoff when the operation is safe
# to retry.
#
# IMPORTANT:
# Retrying a non-idempotent operation can create duplicates.
#
# REMEMBER:
# "Retry transient failures, not every failure."


# ------------------------------------------------------------
# CIRCUIT BREAKER
# ------------------------------------------------------------
# SCENARIO:
# Payment service is down.
# Our API continues sending thousands of requests to it.
#
# PROBLEM:
# We waste threads/connections and may create a cascading failure.
#
# WHAT WE DO:
# Circuit breaker temporarily stops calls after repeated failures.
#
# States:
# Closed -> normal
# Open -> reject/fallback
# Half-Open -> test recovery
#
# REMEMBER:
# "Stop repeatedly calling something that is clearly unhealthy."


# ------------------------------------------------------------
# BULKHEAD
# ------------------------------------------------------------
# SCENARIO:
# Report generation suddenly consumes all worker threads.
# Checkout requests now cannot get a worker.
#
# WHAT WE DO:
# Isolate resources/worker pools for critical workloads.
#
# WHY:
# Failure or overload in one area should not consume everything.
#
# REMEMBER:
# "Give critical workloads their own capacity."


# ------------------------------------------------------------
# GRACEFUL DEGRADATION
# ------------------------------------------------------------
# SCENARIO:
# Recommendation service is down.
# Users still need to purchase products.
#
# WHAT WE DO:
# Disable recommendations but keep checkout working.
#
# WHY:
# Preserve critical business functionality.
#
# REMEMBER:
# "When something fails, keep the important parts alive."


# ------------------------------------------------------------
# SPOF
# ------------------------------------------------------------
# SCENARIO:
# Our entire production system depends on one database server with no
# recovery strategy.
#
# PROBLEM:
# That server fails -> entire system fails.
#
# WHAT WE DO:
# Identify critical single points of failure and design redundancy/recovery
# where justified.
#
# REMEMBER:
# "Ask: what one component can bring down everything?"


# ------------------------------------------------------------
# RTO
# ------------------------------------------------------------
# SCENARIO:
# Payment system fails completely.
# Business says it must be restored within 30 minutes.
#
# THAT TARGET:
# RTO = 30 minutes.
#
# REMEMBER:
# "How quickly must we recover?"


# ------------------------------------------------------------
# RPO
# ------------------------------------------------------------
# SCENARIO:
# Company says a disaster may cause at most 5 minutes of transaction data loss.
#
# THAT TARGET:
# RPO = 5 minutes.
#
# REMEMBER:
# "How much recent data can we afford to lose?"


# ============================================================
# 14. OBSERVABILITY
# ============================================================

# ------------------------------------------------------------
# OBSERVABILITY
# ------------------------------------------------------------
# SCENARIO:
# Users report that checkout is slow.
# You cannot reproduce it locally.
#
# PROBLEM:
# Without logs, metrics and traces, production behavior is difficult to explain.
#
# WHAT WE DO:
# Build observability into the system.
#
# REMEMBER:
# "A production system should tell you what it is doing."


# ------------------------------------------------------------
# LOGS
# ------------------------------------------------------------
# SCENARIO:
# One API returns 500 errors at 2 AM.
#
# WHAT WE NEED:
# Timestamp, request/correlation ID, endpoint, error and useful context.
#
# WHAT WE DO:
# Use structured logs and centralized log collection.
#
# REMEMBER:
# "Logs tell you what happened."


# ------------------------------------------------------------
# METRICS
# ------------------------------------------------------------
# SCENARIO:
# API feels slower than usual.
#
# WHAT WE NEED:
# Request rate, error rate, CPU, memory, latency, DB connection usage, etc.
#
# WHY:
# Metrics show trends and system health.
#
# REMEMBER:
# "Metrics tell you how much/how often."


# ------------------------------------------------------------
# TRACING
# ------------------------------------------------------------
# SCENARIO:
# One request travels:
#
# API -> Order Service -> Payment -> Inventory -> DB
#
# Overall request = 5 seconds.
#
# PROBLEM:
# Which component consumed 4.5 seconds?
#
# WHAT WE DO:
# Distributed tracing with trace IDs and spans.
#
# REMEMBER:
# "Tracing tells you where the request spent its time."


# ------------------------------------------------------------
# CORRELATION ID
# ------------------------------------------------------------
# SCENARIO:
# A user request passes through five services.
# Each service creates separate logs.
#
# WHAT WE DO:
# Propagate one request/correlation ID through the flow.
#
# WHY:
# Search all related logs using the same identifier.
#
# REMEMBER:
# "One request -> one searchable trail."


# ------------------------------------------------------------
# SLI / SLO / SLA
# ------------------------------------------------------------
# SCENARIO:
# Business cares about API availability and latency.
#
# SLI:
# What we measure, e.g. successful request percentage.
#
# SLO:
# Our target, e.g. 99.9% successful requests.
#
# SLA:
# Formal commitment to a customer/business, potentially with consequences.
#
# REMEMBER:
# "SLI = measure, SLO = target, SLA = commitment."


# ============================================================
# 15. PERFORMANCE ENGINEERING
# ============================================================

# ------------------------------------------------------------
# LATENCY
# ------------------------------------------------------------
# SCENARIO:
# User clicks "Generate Report" and waits 8 seconds.
#
# WHAT WE MEASURE:
# Request latency.
#
# WHY:
# Lower latency generally improves user experience, but the required target
# depends on the business operation.
#
# REMEMBER:
# "Latency = how long one operation takes."


# ------------------------------------------------------------
# THROUGHPUT
# ------------------------------------------------------------
# SCENARIO:
# Our API processes 5,000 requests every second.
#
# THAT IS:
# Throughput = 5,000 requests/second.
#
# REMEMBER:
# "Throughput = how much work the system handles per unit time."


# ------------------------------------------------------------
# QPS / RPS / TPS
# ------------------------------------------------------------
# QPS = queries per second.
# RPS = requests per second.
# TPS = transactions per second.
#
# SCENARIO:
# During peak time, our system receives 20,000 API requests/second.
# We need this number for capacity planning.


# ------------------------------------------------------------
# P50 / P95 / P99
# ------------------------------------------------------------
# SCENARIO:
# Most API calls take 100 ms, but some users wait 5 seconds.
#
# PROBLEM:
# Average latency can hide bad experiences.
#
# WHAT WE DO:
# Track percentiles:
# P50 -> median
# P95 -> 95% are at or below this latency
# P99 -> 99% are at or below this latency
#
# REMEMBER:
# "Percentiles expose tail latency."


# ------------------------------------------------------------
# BOTTLENECK
# ------------------------------------------------------------
# SCENARIO:
# API servers have 20% CPU usage, but database CPU is 95%.
#
# PROBLEM:
# Increasing API servers won't solve the real bottleneck.
#
# WHAT WE DO:
# Identify the limiting resource before scaling.
#
# REMEMBER:
# "Scale the bottleneck, not the component you happen to notice first."


# ------------------------------------------------------------
# PROFILING
# ------------------------------------------------------------
# SCENARIO:
# A Python API takes 3 seconds.
# We don't know whether CPU, DB calls or serialization is responsible.
#
# WHAT WE DO:
# Profile and measure actual time/resource usage.
#
# WHY:
# Optimization should be based on evidence.
#
# REMEMBER:
# "Measure before optimizing."


# ============================================================
# 16. NETWORKING
# ============================================================

# ------------------------------------------------------------
# DNS
# ------------------------------------------------------------
# SCENARIO:
# User enters:
# api.company.com
#
# The browser needs an IP address to connect to.
#
# WHAT HAPPENS:
# DNS resolves the domain name to an IP/address destination.
#
# REMEMBER:
# "DNS answers: where is this service?"


# ------------------------------------------------------------
# TCP
# ------------------------------------------------------------
# SCENARIO:
# Our backend needs reliable, ordered communication with a database/API.
#
# WHAT WE USE:
# TCP is commonly used for reliable transport.
#
# REMEMBER:
# "TCP gives reliable ordered byte-stream transport."


# ------------------------------------------------------------
# UDP
# ------------------------------------------------------------
# SCENARIO:
# An application values low overhead/latency and can tolerate or implement
# its own reliability behavior.
#
# WHAT WE CONSIDER:
# UDP can be appropriate for certain workloads.
#
# REMEMBER:
# "UDP trades transport guarantees for lower overhead."


# ------------------------------------------------------------
# HTTP
# ------------------------------------------------------------
# SCENARIO:
# Angular frontend sends:
#
# GET /assignments/123
#
# Backend returns an HTTP response.
#
# WHAT WE USE:
# HTTP is the application-layer protocol carrying the request/response.
#
# REMEMBER:
# "HTTP defines the web request/response conversation."


# ------------------------------------------------------------
# HTTPS
# ------------------------------------------------------------
# SCENARIO:
# Browser sends credentials to API.
#
# WHAT WE NEED:
# Encrypt traffic and protect integrity/authentication of the connection.
#
# WHAT WE USE:
# HTTP over TLS = HTTPS.
#
# REMEMBER:
# "HTTPS protects HTTP traffic in transit."


# ------------------------------------------------------------
# REVERSE PROXY
# ------------------------------------------------------------
# SCENARIO:
# Internet users should not directly reach every internal application server.
#
# WHAT WE DO:
# Put a reverse proxy/load balancer in front.
#
# Client -> Reverse Proxy -> Backend
#
# USES:
# TLS termination, routing, load balancing, security, compression.
#
# REMEMBER:
# "The proxy receives the request and decides where it goes."


# ------------------------------------------------------------
# NAT
# ------------------------------------------------------------
# SCENARIO:
# Backend server is in a private network and needs to call an external API.
# We don't want the private server directly exposed to the internet.
#
# WHAT WE DO:
# Use appropriate NAT architecture for outbound connectivity.
#
# REMEMBER:
# "Private machines can reach outward without becoming directly public."


# ============================================================
# 17. ASYNC & BACKGROUND PROCESSING
# ============================================================

# ------------------------------------------------------------
# SYNCHRONOUS
# ------------------------------------------------------------
# SCENARIO:
# Client calls GET /user/123.
# Query takes 20 ms.
# Client needs the answer immediately.
#
# WHAT WE DO:
# Process synchronously and return the result.
#
# REMEMBER:
# "Caller waits because it needs the result now."


# ------------------------------------------------------------
# ASYNCHRONOUS
# ------------------------------------------------------------
# SCENARIO:
# User uploads 10,000 records.
# Processing takes 2 minutes.
#
# WHAT WE DO:
# Accept request, create a background job and return a job ID.
#
# WHY:
# User does not need to keep an HTTP connection open for two minutes.
#
# REMEMBER:
# "If the work doesn't need to finish before the response, consider async."


# ------------------------------------------------------------
# PYTHON ASYNCIO
# ------------------------------------------------------------
# SCENARIO:
# Our API needs to call 20 external services.
# Each call spends most of its time waiting for network I/O.
#
# WHAT WE DO:
# Async I/O can allow the application to make progress on other work
# while one operation is waiting.
#
# WHY:
# Efficient concurrency for I/O-bound workloads when the libraries are
# async-compatible.
#
# REMEMBER:
# "Async is mainly about not wasting time waiting for I/O."


# ------------------------------------------------------------
# BACKGROUND JOB
# ------------------------------------------------------------
# SCENARIO:
# User requests a PDF report.
#
# API:
# 1. Creates job.
# 2. Returns job_id.
#
# Worker:
# 3. Generates PDF.
# 4. Uploads to S3.
# 5. Updates job status.
#
# WHY:
# Heavy/slow work leaves the request path.
#
# REMEMBER:
# "Request quickly; process heavy work separately."


# ------------------------------------------------------------
# WORKER
# ------------------------------------------------------------
# SCENARIO:
# Queue contains 100,000 report jobs.
#
# WHAT WE DO:
# Run multiple worker processes/containers that consume jobs.
#
# WHY:
# Increase processing capacity independently from API traffic.
#
# REMEMBER:
# "Workers turn queued work into completed work."


# ------------------------------------------------------------
# SCHEDULER
# ------------------------------------------------------------
# SCENARIO:
# Every night at 1 AM we need to generate a report.
#
# WHAT WE DO:
# Use cron/cloud scheduler/job scheduler.
#
# WHY:
# Automatically trigger scheduled work.
#
# REMEMBER:
# "Scheduler decides when the job starts."


# ============================================================
# 18. CLOUD ARCHITECTURE
# ============================================================

# ------------------------------------------------------------
# EC2 VS CONTAINERS VS LAMBDA
# ------------------------------------------------------------
# SCENARIO:
# We need to deploy a backend.
#
# EC2:
# We want more control over the server/OS.
#
# Containers:
# We want a packaged application with consistent runtime behavior.
#
# Lambda:
# Work is event-driven and fits serverless execution characteristics.
#
# ARCHITECT MINDSET:
# Don't ask "Which service is popular?"
# Ask "Which execution model fits the workload and operational needs?"


# ------------------------------------------------------------
# VPC
# ------------------------------------------------------------
# SCENARIO:
# Our production application has public APIs and private databases.
#
# WHAT WE DO:
# Put resources inside an isolated cloud network with subnets and routing.
#
# WHY:
# Control network boundaries and traffic paths.
#
# REMEMBER:
# "VPC is the network boundary for cloud resources."


# ------------------------------------------------------------
# PUBLIC VS PRIVATE SUBNET
# ------------------------------------------------------------
# SCENARIO:
# Load balancer must receive internet traffic.
# Database must not be directly reachable from the internet.
#
# WHAT WE DO:
# Place internet-facing components appropriately and databases in private
# network segments.
#
# REMEMBER:
# "Public entry point; private sensitive resources."


# ------------------------------------------------------------
# SECURITY GROUP
# ------------------------------------------------------------
# SCENARIO:
# Database should accept traffic only from the application servers.
#
# WHAT WE DO:
# Configure network rules to allow only required traffic.
#
# REMEMBER:
# "Allow the traffic that is required, deny unnecessary access."


# ------------------------------------------------------------
# S3 / OBJECT STORAGE
# ------------------------------------------------------------
# SCENARIO:
# Users upload PDFs, images and generated reports.
# Storing huge files directly inside the relational database increases DB
# size and operational cost.
#
# WHAT WE DO:
# Use object storage such as S3 for suitable files.
#
# REMEMBER:
# "Files often belong in object storage, metadata in the database."


# ------------------------------------------------------------
# RDS / AURORA
# ------------------------------------------------------------
# SCENARIO:
# Our order application needs relational transactions, SQL joins and
# structured constraints.
#
# WHAT WE DO:
# Use a managed relational database service where appropriate.
#
# WHY:
# Managed backups, patching/operations and relational database capabilities.
#
# REMEMBER:
# "Managed SQL database for transactional relational workloads."


# ------------------------------------------------------------
# DYNAMODB
# ------------------------------------------------------------
# SCENARIO:
# We need very high-scale access using predictable key-based patterns.
#
# WHAT WE CONSIDER:
# DynamoDB or another suitable NoSQL store.
#
# REMEMBER:
# "Model around access patterns, not tables copied from relational design."


# ------------------------------------------------------------
# ELASTICACHE
# ------------------------------------------------------------
# SCENARIO:
# Thousands of requests repeatedly need the same hot data.
#
# WHAT WE DO:
# Use a managed in-memory data store/cache where appropriate.
#
# REMEMBER:
# "Fast temporary/shared data access to reduce pressure on primary storage."


# ------------------------------------------------------------
# SQS
# ------------------------------------------------------------
# SCENARIO:
# Order service needs invoice generation but shouldn't wait for it.
#
# WHAT WE DO:
# Send a job to a managed queue such as SQS.
#
# REMEMBER:
# "Queue work so producers and consumers are decoupled."


# ------------------------------------------------------------
# SNS
# ------------------------------------------------------------
# SCENARIO:
# One event needs to notify email, analytics and another service.
#
# WHAT WE WANT:
# Fan-out/publish-subscribe behavior.
#
# REMEMBER:
# "One message can notify multiple subscribers."


# ------------------------------------------------------------
# EVENTBRIDGE
# ------------------------------------------------------------
# SCENARIO:
# Many AWS/application services produce business events.
# Different consumers need selected events.
#
# WHAT WE DO:
# Route events through an event bus where appropriate.
#
# REMEMBER:
# "Central event routing based on event rules."


# ------------------------------------------------------------
# IAM
# ------------------------------------------------------------
# SCENARIO:
# A report-generation service needs access to one S3 bucket.
#
# BAD:
# Give full AWS administrator permissions.
#
# GOOD:
# Give only required S3 permissions.
#
# REMEMBER:
# "Cloud identity permissions should follow least privilege."


# ============================================================
# 19. DOCKER & KUBERNETES
# ============================================================

# ------------------------------------------------------------
# DOCKER IMAGE
# ------------------------------------------------------------
# SCENARIO:
# Developer's machine has Python 3.12, but production has Python 3.10.
#
# PROBLEM:
# "Works on my machine."
#
# WHAT WE DO:
# Package application + dependencies into a consistent container image.
#
# REMEMBER:
# "Package the environment with the application."


# ------------------------------------------------------------
# MULTI-STAGE BUILD
# ------------------------------------------------------------
# SCENARIO:
# Building our application requires compilers/build tools, but production
# only needs the runtime.
#
# WHAT WE DO:
# Use a build stage and a smaller runtime stage.
#
# WHY:
# Smaller image and reduced attack surface.
#
# REMEMBER:
# "Build with many tools; run with only what is needed."


# ------------------------------------------------------------
# KUBERNETES POD
# ------------------------------------------------------------
# SCENARIO:
# We need to run our backend containers on a Kubernetes cluster.
#
# WHAT WE DO:
# Kubernetes schedules containers inside pods.
#
# REMEMBER:
# "Pod is the basic deployable execution unit in Kubernetes."


# ------------------------------------------------------------
# KUBERNETES DEPLOYMENT
# ------------------------------------------------------------
# SCENARIO:
# We want 5 copies of our API running.
# If one crashes, we want it recreated.
#
# WHAT WE DO:
# Use a Deployment to manage replicated stateless application pods.
#
# REMEMBER:
# "Deployment manages desired replicas and rollouts."


# ------------------------------------------------------------
# KUBERNETES SERVICE
# ------------------------------------------------------------
# SCENARIO:
# Pods can be replaced and their IPs can change.
# Other applications need a stable way to reach them.
#
# WHAT WE DO:
# Use a Service for stable discovery/network access.
#
# REMEMBER:
# "Pods change; Service gives a stable endpoint."


# ------------------------------------------------------------
# INGRESS
# ------------------------------------------------------------
# SCENARIO:
# One domain receives:
# /users -> user service
# /orders -> order service
# /reports -> report service
#
# WHAT WE DO:
# Use an ingress/routing layer as appropriate.
#
# REMEMBER:
# "Route external HTTP traffic to internal services."


# ------------------------------------------------------------
# HPA
# ------------------------------------------------------------
# SCENARIO:
# Normal traffic needs 3 API pods.
# During peak time CPU/request load increases significantly.
#
# WHAT WE DO:
# Configure horizontal autoscaling based on suitable metrics.
#
# REMEMBER:
# "Automatically add/remove replicas based on demand."


# ============================================================
# 20. CI/CD & DEVOPS
# ============================================================

# ------------------------------------------------------------
# CI
# ------------------------------------------------------------
# SCENARIO:
# Five developers merge code every day.
# One developer's change breaks tests.
#
# WHAT WE DO:
# Automatically build and test changes in CI.
#
# WHY:
# Find problems early.
#
# REMEMBER:
# "Every change should be automatically validated."


# ------------------------------------------------------------
# CD
# ------------------------------------------------------------
# SCENARIO:
# Tests pass, but developers manually copy files to production.
#
# PROBLEM:
# Manual deployments are inconsistent and error-prone.
#
# WHAT WE DO:
# Automate release/deployment steps.
#
# REMEMBER:
# "Make delivery repeatable."


# ------------------------------------------------------------
# ROLLING DEPLOYMENT
# ------------------------------------------------------------
# SCENARIO:
# We have 10 backend instances.
# We release version 2.
#
# WHAT WE DO:
# Replace instances gradually rather than all at once.
#
# REMEMBER:
# "Update gradually."


# ------------------------------------------------------------
# BLUE/GREEN
# ------------------------------------------------------------
# SCENARIO:
# Version 1 is serving production traffic.
# Version 2 is deployed separately and ready.
#
# WHAT WE DO:
# Switch traffic from blue to green.
#
# WHY:
# Fast rollback by switching traffic back when appropriate.
#
# REMEMBER:
# "Keep old and new environments available for a controlled switch."


# ------------------------------------------------------------
# CANARY
# ------------------------------------------------------------
# SCENARIO:
# We don't trust a new version enough to send 100% traffic immediately.
#
# WHAT WE DO:
# Send a small percentage of traffic to the new version first.
#
# WHY:
# Detect problems before broad rollout.
#
# REMEMBER:
# "Let a small percentage of real traffic test the release."


# ------------------------------------------------------------
# FEATURE FLAG
# ------------------------------------------------------------
# SCENARIO:
# New functionality is deployed but product wants it enabled for only
# internal users initially.
#
# WHAT WE DO:
# Use a feature flag.
#
# WHY:
# Deployment and feature release become separate decisions.
#
# REMEMBER:
# "Code can be deployed without immediately exposing the feature."


# ============================================================
# 21. TESTING
# ============================================================

# ------------------------------------------------------------
# UNIT TEST
# ------------------------------------------------------------
# SCENARIO:
# Discount calculation is pure business logic.
#
# WHAT WE DO:
# Test the function with many inputs without needing a real database.
#
# WHY:
# Fast feedback and isolated correctness checks.
#
# REMEMBER:
# "Test small pieces quickly."


# ------------------------------------------------------------
# INTEGRATION TEST
# ------------------------------------------------------------
# SCENARIO:
# Our repository code interacts with PostgreSQL.
#
# PROBLEM:
# Unit tests with mocks may not detect SQL/schema/database behavior issues.
#
# WHAT WE DO:
# Test the real integration with a controlled test database/environment.
#
# REMEMBER:
# "Check whether components actually work together."


# ------------------------------------------------------------
# CONTRACT TEST
# ------------------------------------------------------------
# SCENARIO:
# Order Service expects:
# status = "PAID"
#
# Payment Service changes it to:
# payment_status = "SUCCESS"
#
# PROBLEM:
# Producer changed the contract and consumer breaks.
#
# WHAT WE DO:
# Contract tests validate expectations between services.
#
# REMEMBER:
# "Make sure producer and consumer agree on the contract."


# ------------------------------------------------------------
# E2E TEST
# ------------------------------------------------------------
# SCENARIO:
# User:
# Login -> Create order -> Pay -> View order.
#
# WHAT WE DO:
# Test the complete business flow.
#
# TRADE-OFF:
# More realistic but slower and more fragile than unit tests.
#
# REMEMBER:
# "Validate the entire journey."


# ------------------------------------------------------------
# LOAD TEST
# ------------------------------------------------------------
# SCENARIO:
# Production expects 5,000 requests/second.
#
# WHAT WE DO:
# Generate representative traffic and measure latency/errors/resources.
#
# REMEMBER:
# "Test expected load before production discovers the limit."


# ------------------------------------------------------------
# STRESS TEST
# ------------------------------------------------------------
# SCENARIO:
# We keep increasing traffic until the system begins failing.
#
# WHY:
# Find capacity limits and failure behavior.
#
# REMEMBER:
# "Push beyond normal capacity to discover the breaking point."


# ============================================================
# 22. DESIGN PATTERNS
# ============================================================

# ------------------------------------------------------------
# FACTORY
# ------------------------------------------------------------
# SCENARIO:
# Application supports Email, SMS and Push notifications.
# Caller shouldn't know all construction details.
#
# WHAT WE DO:
# Factory selects/creates the correct notification implementation.
#
# REMEMBER:
# "Centralize creation when object creation has meaningful rules."


# ------------------------------------------------------------
# ADAPTER
# ------------------------------------------------------------
# SCENARIO:
# Our application expects:
# send(message)
#
# Third-party provider exposes:
# publish_sms(phone, text)
#
# WHAT WE DO:
# Create an adapter that translates our interface to the provider's interface.
#
# REMEMBER:
# "Make incompatible interfaces work together."


# ------------------------------------------------------------
# FACADE
# ------------------------------------------------------------
# SCENARIO:
# Creating an order requires inventory, payment, shipping and notification.
#
# WHAT WE DO:
# Provide a simpler OrderFacade/Service to coordinate the complex subsystem.
#
# REMEMBER:
# "Hide complexity behind a simple interface."


# ------------------------------------------------------------
# DECORATOR
# ------------------------------------------------------------
# SCENARIO:
# We want to add timing/logging to many functions without modifying their
# business logic.
#
# WHAT WE DO:
# Use a decorator.
#
# REMEMBER:
# "Wrap behavior around existing behavior."


# ------------------------------------------------------------
# STRATEGY
# ------------------------------------------------------------
# SCENARIO:
# Pricing changes based on:
# RegularCustomer
# PremiumCustomer
# FestivalSale
#
# WHAT WE DO:
# Put each pricing algorithm behind a strategy interface.
#
# WHY:
# Swap algorithms without a giant if/else block.
#
# REMEMBER:
# "Encapsulate interchangeable business rules."


# ------------------------------------------------------------
# REPOSITORY
# ------------------------------------------------------------
# SCENARIO:
# Business service should not contain raw database details everywhere.
#
# WHAT WE DO:
# Put persistence operations behind a repository abstraction where useful.
#
# REMEMBER:
# "Separate business decisions from persistence details."


# ------------------------------------------------------------
# DEPENDENCY INJECTION
# ------------------------------------------------------------
# SCENARIO:
# OrderService directly creates a MySQL repository.
# Testing becomes difficult because we cannot easily replace it.
#
# WHAT WE DO:
# Supply the repository dependency from outside.
#
# WHY:
# Easier testing and lower coupling.
#
# REMEMBER:
# "Don't force a class to construct every dependency it needs."


# ============================================================
# 23. DOMAIN-DRIVEN DESIGN
# ============================================================

# ------------------------------------------------------------
# DOMAIN
# ------------------------------------------------------------
# SCENARIO:
# Our company operates a telecom assignment platform.
#
# The business rules around assignments, programs and schedules are the
# domain we are solving.
#
# REMEMBER:
# "Domain = the business problem our software exists to solve."


# ------------------------------------------------------------
# SUBDOMAIN
# ------------------------------------------------------------
# SCENARIO:
# Large telecom platform contains:
# Customer Management
# Billing
# Assignments
# Reporting
#
# WHAT WE DO:
# Treat these as meaningful business areas/subdomains.
#
# REMEMBER:
# "Break a large business problem into meaningful business capabilities."


# ------------------------------------------------------------
# BOUNDED CONTEXT
# ------------------------------------------------------------
# SCENARIO:
# "Customer" may mean a billing account in Billing,
# but a service subscriber in Customer Management.
#
# PROBLEM:
# One global model can create confusing meanings.
#
# WHAT WE DO:
# Define models/terms within explicit boundaries.
#
# REMEMBER:
# "The same word can mean different things in different business contexts."


# ------------------------------------------------------------
# ENTITY
# ------------------------------------------------------------
# SCENARIO:
# User with ID 123 changes their name from A to B.
# It is still the same user.
#
# WHAT WE CARE ABOUT:
# Identity, not just current values.
#
# REMEMBER:
# "Entity is identified by identity that persists through changes."


# ------------------------------------------------------------
# VALUE OBJECT
# ------------------------------------------------------------
# SCENARIO:
# Two Money objects both contain ₹500 INR.
# We care about their values, not a unique database identity.
#
# WHAT WE DO:
# Model concepts such as Money, Address or DateRange as value objects where
# appropriate.
#
# REMEMBER:
# "Value objects are defined by what they contain."


# ------------------------------------------------------------
# AGGREGATE
# ------------------------------------------------------------
# SCENARIO:
# An Order has OrderItems.
# Business rules say items must be changed through the Order boundary.
#
# WHAT WE DO:
# Define an aggregate consistency boundary and an aggregate root.
#
# REMEMBER:
# "Aggregate controls a consistency boundary in the domain."


# ------------------------------------------------------------
# DOMAIN EVENT
# ------------------------------------------------------------
# SCENARIO:
# Payment has successfully completed.
#
# WHAT HAPPENED:
# PaymentCompleted.
#
# Other parts of the system may react without Payment Service knowing
# every consumer.
#
# REMEMBER:
# "A domain event says: something meaningful happened."


# ============================================================
# 24. DISTRIBUTED TRANSACTIONS
# ============================================================

# ------------------------------------------------------------
# TWO-PHASE COMMIT
# ------------------------------------------------------------
# SCENARIO:
# One business transaction must coordinate multiple transactional resources.
#
# WHAT WE DO:
# A coordinator uses prepare and commit phases.
#
# PROBLEM:
# Coordination can be expensive/blocking and complex in distributed systems.
#
# REMEMBER:
# "Strong cross-resource coordination comes with operational cost."


# ------------------------------------------------------------
# SAGA
# ------------------------------------------------------------
# SCENARIO:
# Creating an order involves:
# Order -> Payment -> Inventory -> Shipping
#
# Payment succeeds.
# Inventory fails.
#
# PROBLEM:
# We cannot simply roll back a remote database transaction as if everything
# were one local transaction.
#
# WHAT WE DO:
# Use a Saga with compensating actions where appropriate.
#
# Example:
# Payment succeeds -> inventory fails -> refund payment.
#
# REMEMBER:
# "Distributed transaction = local steps + failure compensation."


# ------------------------------------------------------------
# CHOREOGRAPHY
# ------------------------------------------------------------
# SCENARIO:
# OrderCreated event is published.
# Payment and Inventory independently react.
#
# WHAT WE DO:
# Services coordinate through events without a central controller.
#
# REMEMBER:
# "Services react to events and coordinate themselves."


# ------------------------------------------------------------
# ORCHESTRATION
# ------------------------------------------------------------
# SCENARIO:
# A business process has many steps and complex failure rules.
#
# WHAT WE DO:
# A central workflow/orchestrator directs:
# pay -> reserve -> ship -> notify.
#
# REMEMBER:
# "One coordinator controls the workflow."


# ------------------------------------------------------------
# TRANSACTIONAL OUTBOX
# ------------------------------------------------------------
# SCENARIO:
# Order is saved to MySQL.
# Then application tries to publish OrderCreated to Kafka.
# Kafka is down.
#
# PROBLEM:
# DB says order exists, but event was never published.
#
# WHAT WE DO:
# In the same DB transaction:
# 1. Save order.
# 2. Save outgoing event in an outbox table.
#
# A separate publisher sends outbox events later.
#
# WHY:
# Connect database state and outgoing event reliably.
#
# REMEMBER:
# "Save the business change and the event intention together."


# ============================================================
# 25. DATA ARCHITECTURE
# ============================================================

# ------------------------------------------------------------
# OLTP
# ------------------------------------------------------------
# SCENARIO:
# User places an order.
# Database needs frequent inserts/updates and transactional consistency.
#
# WHAT WE NEED:
# OLTP-style database workload.
#
# REMEMBER:
# "OLTP = day-to-day transactions."


# ------------------------------------------------------------
# OLAP
# ------------------------------------------------------------
# SCENARIO:
# Management asks:
# "Show total sales by region for the last 5 years."
#
# PROBLEM:
# Running huge analytical queries directly on the transactional database
# can hurt production.
#
# WHAT WE DO:
# Use analytical storage/workloads where appropriate.
#
# REMEMBER:
# "OLAP = analyze lots of historical data."


# ------------------------------------------------------------
# ETL
# ------------------------------------------------------------
# SCENARIO:
# We collect customer data from System A, transform it and load it into
# a warehouse.
#
# FLOW:
# Extract -> Transform -> Load
#
# REMEMBER:
# "Transform before loading."


# ------------------------------------------------------------
# ELT
# ------------------------------------------------------------
# SCENARIO:
# We load raw data into a powerful analytical platform first and transform
# it there.
#
# FLOW:
# Extract -> Load -> Transform
#
# REMEMBER:
# "Load raw data first, transform later."


# ------------------------------------------------------------
# CDC
# ------------------------------------------------------------
# SCENARIO:
# Customer table has 10 million rows.
# We don't want to copy the entire table every hour just to know what changed.
#
# WHAT WE DO:
# Capture inserts/updates/deletes as changes.
#
# WHY:
# Efficiently stream database changes to downstream systems.
#
# REMEMBER:
# "Send what changed instead of repeatedly copying everything."


# ------------------------------------------------------------
# DATA WAREHOUSE
# ------------------------------------------------------------
# SCENARIO:
# Business wants dashboards, historical analysis and aggregations across
# many systems.
#
# WHAT WE DO:
# Store analytical data in a warehouse designed for those queries.
#
# REMEMBER:
# "Warehouse = organized analytical data."


# ------------------------------------------------------------
# DATA LAKE
# ------------------------------------------------------------
# SCENARIO:
# Company receives logs, JSON, CSV, images and raw events from many sources.
#
# WHAT WE DO:
# Store large amounts of raw/semi-structured data in a data lake/object storage
# architecture.
#
# REMEMBER:
# "Lake = large-scale raw and varied data."


# ------------------------------------------------------------
# STAR SCHEMA
# ------------------------------------------------------------
# SCENARIO:
# Sales analytics needs:
# Sales amount by product, customer, region and date.
#
# WHAT WE DO:
# Central fact table + dimension tables.
#
# REMEMBER:
# "Fact = measurements; dimensions = ways to analyze them."


# ============================================================
# 26. SYSTEM INTEGRATION
# ============================================================

# ------------------------------------------------------------
# REST INTEGRATION
# ------------------------------------------------------------
# SCENARIO:
# Our assignment system needs program data from another service.
#
# WHAT WE DO:
# Call the external REST API.
#
# IMPORTANT:
# Timeout, retry, error handling, authentication and version compatibility.
#
# REMEMBER:
# "External API calls are dependencies, not local functions."


# ------------------------------------------------------------
# SOAP
# ------------------------------------------------------------
# SCENARIO:
# A large enterprise/legacy system exposes employee data using XML SOAP.
#
# WHAT WE DO:
# Integrate with its contract rather than assuming everything is REST.
#
# REMEMBER:
# "Modern architecture still has to integrate with legacy enterprise systems."


# ------------------------------------------------------------
# WEBHOOK
# ------------------------------------------------------------
# SCENARIO:
# Payment provider needs to tell us when payment status changes.
#
# BAD:
# Poll every second for every payment.
#
# WHAT WE DO:
# Give provider an endpoint to call when the event occurs.
#
# REMEMBER:
# "Instead of repeatedly asking, let the provider notify you."


# ------------------------------------------------------------
# SFTP
# ------------------------------------------------------------
# SCENARIO:
# An enterprise partner sends a CSV file every night.
# No API exists.
#
# WHAT WE DO:
# Securely exchange files using SFTP when required.
#
# REMEMBER:
# "Enterprise integration may still be file-based."


# ------------------------------------------------------------
# EXTERNAL API RESILIENCE
# ------------------------------------------------------------
# SCENARIO:
# Our application depends on a third-party service.
# That service becomes slow/unavailable.
#
# WHAT WE NEED:
# Timeout
# Retry where safe
# Exponential backoff
# Circuit breaker
# Idempotency
# Monitoring
# Fallback where possible
#
# REMEMBER:
# "Every external dependency can fail."


# ============================================================
# 27. PRODUCTION ENGINEERING
# ============================================================

# ------------------------------------------------------------
# INCIDENT
# ------------------------------------------------------------
# SCENARIO:
# Production API error rate jumps from 0.1% to 20%.
#
# WHAT WE DO:
# Detect, assess impact, mitigate, communicate and investigate.
#
# REMEMBER:
# "Production incidents require fast stabilization before deep investigation."


# ------------------------------------------------------------
# ROOT CAUSE ANALYSIS
# ------------------------------------------------------------
# SCENARIO:
# API failed because database connections were exhausted.
#
# BAD RCA:
# "Database was down."
#
# BETTER:
# "A deployment increased connection usage, pool limits were too high,
# database reached connection capacity, causing API failures."
#
# REMEMBER:
# "Find the underlying chain of causes, not just the visible symptom."


# ------------------------------------------------------------
# POSTMORTEM
# ------------------------------------------------------------
# SCENARIO:
# Production outage lasted 40 minutes.
#
# WHAT WE DOCUMENT:
# Impact
# Timeline
# Detection
# Root cause
# Contributing factors
# Recovery
# Preventive actions
#
# REMEMBER:
# "Learn from incidents and reduce the chance of recurrence."


# ------------------------------------------------------------
# RUNBOOK
# ------------------------------------------------------------
# SCENARIO:
# Every time a particular queue gets stuck, an engineer has to remember
# 15 manual steps.
#
# WHAT WE DO:
# Document the exact operational procedure.
#
# REMEMBER:
# "Turn repeated operational knowledge into a reliable procedure."


# ------------------------------------------------------------
# BACKUP / RESTORE
# ------------------------------------------------------------
# SCENARIO:
# Someone accidentally deletes important production data.
#
# PROBLEM:
# Backup exists, but nobody has tested restoring it.
#
# WHAT WE DO:
# Maintain backups AND regularly test restoration.
#
# REMEMBER:
# "A backup is useful only if it can actually be restored."


# ------------------------------------------------------------
# DISASTER RECOVERY
# ------------------------------------------------------------
# SCENARIO:
# Primary region becomes unavailable.
#
# WHAT WE NEED:
# A tested strategy to recover service and data according to RTO/RPO.
#
# REMEMBER:
# "Disaster recovery is a plan + architecture + testing, not just a backup."


# ============================================================
# 28. ARCHITECTURE DECISION MAKING
# ============================================================

# ------------------------------------------------------------
# MONOLITH VS MICROSERVICES
# ------------------------------------------------------------
# SCENARIO:
# Team has 5 developers and 20,000 users.
#
# QUESTION:
# Should we create 20 microservices?
#
# ARCHITECT THINKING:
# Probably not automatically.
# Consider team size, domain boundaries, deployment independence,
# scaling requirements and operational maturity.
#
# REMEMBER:
# "Architecture follows requirements, not fashion."


# ------------------------------------------------------------
# SQL VS NOSQL
# ------------------------------------------------------------
# SCENARIO:
# We need complex joins, strong transactions and relational constraints.
#
# WHAT WE CONSIDER:
# Relational database is a natural fit.
#
# Different scenario:
# Extremely high-scale key/value access with predictable patterns.
# NoSQL may be a better fit.
#
# REMEMBER:
# "Choose storage based on consistency, access patterns, scale and query needs."


# ------------------------------------------------------------
# REDIS VS DATABASE
# ------------------------------------------------------------
# SCENARIO:
# Product catalog is read 100,000 times/minute but changes rarely.
#
# WHAT WE CONSIDER:
# Redis can reduce repeated DB reads.
#
# BUT:
# Source of truth may remain the database.
#
# REMEMBER:
# "Cache is usually an acceleration layer, not automatically the source of truth."


# ------------------------------------------------------------
# KAFKA VS RABBITMQ / QUEUE
# ------------------------------------------------------------
# SCENARIO:
# We need a durable event stream where many consumers process large volumes
# and events may need replay.
#
# WHAT WE CONSIDER:
# Kafka-like event streaming architecture.
#
# Different scenario:
# We simply need reliable asynchronous task delivery to workers.
#
# WHAT WE CONSIDER:
# A traditional queue may be simpler.
#
# REMEMBER:
# "Choose messaging technology based on delivery, ordering, replay,
# throughput and consumer requirements."


# ------------------------------------------------------------
# SYNC VS ASYNC
# ------------------------------------------------------------
# SCENARIO:
# Login request needs an immediate success/failure response.
#
# WHAT WE DO:
# Synchronous.
#
# Scenario:
# Generate a 500 MB report.
#
# WHAT WE DO:
# Usually asynchronous/background processing.
#
# REMEMBER:
# "If the caller needs the result now, sync may fit; otherwise consider async."


# ------------------------------------------------------------
# COST AS AN ARCHITECTURE CONSTRAINT
# ------------------------------------------------------------
# SCENARIO:
# Two architectures satisfy the technical requirements.
#
# Architecture A:
# Very complex multi-region infrastructure.
#
# Architecture B:
# Simpler architecture with adequate availability and capacity.
#
# WHAT WE DO:
# Choose based on business requirements, risk and cost.
#
# REMEMBER:
# "The technically biggest architecture is not automatically the best."


# ============================================================
# 29. ARCHITECTURE DOCUMENTATION
# ============================================================

# ------------------------------------------------------------
# BRD
# ------------------------------------------------------------
# SCENARIO:
# Business says:
# "We need to reduce manual assignment processing."
#
# BRD explains the business goal, problem and high-level requirements.
#
# REMEMBER:
# "BRD explains the business need."


# ------------------------------------------------------------
# FRD
# ------------------------------------------------------------
# SCENARIO:
# Business requirement is approved.
# Now the team needs to describe exactly what the system should do.
#
# FRD covers functional behavior and requirements.
#
# REMEMBER:
# "FRD explains what the system must do."


# ------------------------------------------------------------
# HLD
# ------------------------------------------------------------
# SCENARIO:
# We need to design the complete backend.
#
# HLD shows:
# Client
# API Gateway
# Backend services
# Database
# Cache
# Queue
# Object storage
# External systems
#
# REMEMBER:
# "HLD explains the major building blocks and how they interact."


# ------------------------------------------------------------
# LLD
# ------------------------------------------------------------
# SCENARIO:
# Developers now need to implement the Assignment module.
#
# LLD describes:
# classes/modules
# interfaces
# API details
# DB schema
# queries
# sequence flows
# validations
#
# REMEMBER:
# "LLD gets close enough to implementation for engineers to build it."


# ------------------------------------------------------------
# ADR
# ------------------------------------------------------------
# SCENARIO:
# Team debates PostgreSQL vs MongoDB for a new service.
#
# Instead of relying on memory, document:
# Context
# Decision
# Alternatives
# Trade-offs
# Consequences
#
# REMEMBER:
# "ADR records why an architectural decision was made."


# ------------------------------------------------------------
# SEQUENCE DIAGRAM
# ------------------------------------------------------------
# SCENARIO:
# User creates order.
#
# User -> API -> Order Service -> Payment -> DB
#
# A sequence diagram shows who calls whom and in what order.
#
# REMEMBER:
# "Sequence diagram = interaction over time."


# ------------------------------------------------------------
# ER DIAGRAM
# ------------------------------------------------------------
# SCENARIO:
# Developers need to understand relationships between:
# Users
# Assignments
# Programs
# Schedules
#
# WHAT WE DO:
# Draw entities, keys and relationships.
#
# REMEMBER:
# "ERD = database relationships visually."


# ============================================================
# 30. LEAD ENGINEER SKILLS
# ============================================================

# ------------------------------------------------------------
# CODE REVIEW
# ------------------------------------------------------------
# SCENARIO:
# Developer submits code that works but creates one DB query inside a loop.
#
# JUNIOR REVIEW:
# "Formatting looks good."
#
# LEAD REVIEW:
# "This creates N+1 queries. What happens with 100,000 users?"
#
# REMEMBER:
# "Review correctness, security, performance, maintainability and design."


# ------------------------------------------------------------
# TECHNICAL DEBT
# ------------------------------------------------------------
# SCENARIO:
# Team ships a quick implementation because a release is urgent.
# Six months later, every change requires touching the same fragile code.
#
# WHAT WE DO:
# Make the debt visible, prioritize it and pay it down deliberately.
#
# REMEMBER:
# "Technical debt is future engineering cost, not free speed."


# ------------------------------------------------------------
# ESTIMATION
# ------------------------------------------------------------
# SCENARIO:
# Manager asks:
# "Can we finish this feature in 2 days?"
#
# LEAD THINKING:
# Break it into API, DB, frontend, integration, tests, deployment and risks.
#
# REMEMBER:
# "Estimate the work and uncertainty, not just the coding time."


# ------------------------------------------------------------
# MENTORING
# ------------------------------------------------------------
# SCENARIO:
# Junior developer asks:
# "Why are we using a transaction here?"
#
# WE DON'T JUST SAY:
# "Because architect said so."
#
# WE EXPLAIN:
# "Two updates must succeed together. If one fails, we don't want partial data."
#
# REMEMBER:
# "Teach the reasoning so the engineer can make the next decision alone."


# ------------------------------------------------------------
# TECHNICAL COMMUNICATION
# ------------------------------------------------------------
# SCENARIO:
# Same architecture must be explained to:
# Developer
# Engineering Manager
# Client
#
# WHAT WE DO:
# Developer -> implementation details
# Manager -> delivery/risk/cost
# Client -> business outcome/trade-offs
#
# REMEMBER:
# "Same architecture, different language for different audiences."


# ------------------------------------------------------------
# OWNERSHIP
# ------------------------------------------------------------
# SCENARIO:
# Your ticket says "implement API."
# But production API is slow because the database query is inefficient.
#
# SENIOR/LEAD BEHAVIOR:
# Don't say "DB is someone else's problem."
# Investigate and drive the issue to resolution.
#
# REMEMBER:
# "Own the outcome, not just the ticket."


# ============================================================
# 31. ARCHITECT MASTER CHECKLIST — USE THIS ON EVERY SYSTEM
# ============================================================

# SCENARIO:
# Business gives you a new requirement:
#
# "We need a bulk upload system for 50,000 users."
#
# Before writing code, ask:
#
# 1. REQUIREMENTS
#    What exactly should happen?
#
# 2. SCALE
#    50,000 now. What about 500,000 later?
#
# 3. API
#    How will upload/status/results be exposed?
#
# 4. DATABASE
#    What tables/indexes/transactions are required?
#
# 5. CONCURRENCY
#    What if two uploads modify the same user?
#
# 6. ASYNC
#    Should processing happen in the request or a background worker?
#
# 7. QUEUE
#    Do we need buffering/retries?
#
# 8. CACHING
#    Is any repeated read worth caching?
#
# 9. FAILURE
#    What happens when one record fails?
#    What happens when the DB/external API fails?
#
# 10. IDEMPOTENCY
#     What happens if the upload is submitted twice?
#
# 11. SECURITY
#     Who can upload?
#     How are files validated?
#
# 12. OBSERVABILITY
#     How do we know which records failed and why?
#
# 13. PERFORMANCE
#     How long should 50,000 records take?
#
# 14. DEPLOYMENT
#     How will we release safely?
#
# 15. RECOVERY
#     Can failed jobs be retried/resumed?
#
# 16. COST
#     What infrastructure is required?
#
# 17. MAINTAINABILITY
#     Can another engineer understand and modify it?
#
# REMEMBER:
# "An architect thinks about the whole lifecycle, not only the happy path."


# ============================================================
# 32. ONE-LINE SCENARIO REVISION
# ============================================================

# Race condition:
# Two users update the same data at the same time -> use proper concurrency control.
#
# Deadlock:
# Two transactions hold locks the other needs -> consistent lock ordering/retry.
#
# N+1:
# 10,000 users cause 10,001 queries -> batch/JOIN/prefetch.
#
# Cache stampede:
# Popular key expires and thousands hit DB simultaneously -> protect cache/DB.
#
# Idempotency:
# Network retry might duplicate payment/order -> idempotency key/state.
#
# Circuit breaker:
# Dependency is failing repeatedly -> stop hammering it temporarily.
#
# Bulkhead:
# One workload consumes all resources -> isolate capacity.
#
# CQRS:
# Read and write needs are very different -> separate models/paths.
#
# Saga:
# One business transaction crosses services -> local transactions + compensation.
#
# Outbox:
# DB update succeeds but event publish fails -> store event intention in same DB transaction.
#
# Sharding:
# One DB cannot handle required scale -> split data across nodes.
#
# Replication:
# One data copy is risky -> maintain replicas/backups as required.
#
# CAP:
# Network partition occurs -> consistency/availability behavior must be chosen.
#
# Eventual consistency:
# Replicas can temporarily disagree -> acceptable when business allows it.
#
# Stateless:
# Any server should handle the request -> don't depend on local instance state.
#
# Rate limiting:
# One client sends too much traffic -> limit consumption.
#
# Load balancing:
# One server is overloaded -> distribute traffic.
#
# P95:
# Averages hide slow users -> measure latency percentiles.
#
# RTO:
# "How fast must we recover?"
#
# RPO:
# "How much data can we afford to lose?"
#
# SLI:
# "What are we measuring?"
#
# SLO:
# "What target do we want?"
#
# SLA:
# "What formal commitment do we make?"
#
# Transaction:
# Multiple DB changes must remain consistent -> commit together.
#
# Optimistic locking:
# Conflicts are uncommon -> detect version changes at update time.
#
# Pessimistic locking:
# Concurrent modification must be prevented -> lock during transaction.
#
# Async processing:
# Work takes too long for HTTP request -> queue + worker.
#
# CDN:
# Users download the same static content globally -> cache near users.
#
# Connection pool:
# Creating DB connections repeatedly is expensive -> reuse controlled connections.
#
# EXPLAIN:
# Query became slow -> inspect database execution plan.
#
# Least privilege:
# Service needs one permission -> don't give it administrator access.
#
# Feature flag:
# Code is deployed but feature isn't ready for everyone -> control exposure separately.
#
# Transactional outbox:
# Need DB update + event reliably -> write both to local DB transaction first.


# ============================================================
# FINAL ARCHITECT MINDSET
# ============================================================

# Imagine you are asked:
#
# "Build a backend for 1 million users."
#
# A normal developer may ask:
# "Which framework should I use?"
#
# A senior developer asks:
# "What APIs and database design do we need?"
#
# A lead engineer asks:
# "How will we test, deploy, monitor and maintain it?"
#
# An architect asks:
#
# "What are the business requirements?"
# "How much traffic?"
# "How much data?"
# "What latency is acceptable?"
# "What must be strongly consistent?"
# "What can eventually become consistent?"
# "What happens when the DB fails?"
# "What happens when the external API fails?"
# "How do we prevent duplicate operations?"
# "How do we scale to 10x?"
# "How do we secure it?"
# "How do we observe it?"
# "How do we recover it?"
# "How much will it cost?"
# "Can the team actually operate this?"
#
#
# FINAL RULE:
#
# Good architecture is NOT:
#     "Use microservices + Kafka + Kubernetes + Redis because they are popular."
#
# Good architecture IS:
#     "Choose the simplest design that satisfies the real business,
#      scale, reliability, security, operational and cost requirements."
#
#
# STUDY ORDER:
#
# Python fundamentals
#       ↓
# API design
#       ↓
# SQL + database internals
#       ↓
# Transactions + concurrency
#       ↓
# Caching
#       ↓
# Async + queues
#       ↓
# Performance
#       ↓
# Security
#       ↓
# Distributed systems
#       ↓
# System design
#       ↓
# Cloud architecture
#       ↓
# Reliability + observability
#       ↓
# DDD + architecture patterns
#       ↓
# Leadership + architecture decisions
#
# This is the progression from:
#
# "I can write backend code."
#             ->
# "I can build production systems."
#             ->
# "I can lead backend engineering."
#             ->
# "I can design systems and make architecture decisions."
