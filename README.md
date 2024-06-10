# Supabase Client Integration and CRUD Operations

This repository provides a guide and implementation for integrating a Supabase client into a Python application, along with performing basic CRUD (Create, Read, Update, Delete) operations on a "todos" table.

## Overview

Supabase is an open-source Firebase alternative that offers various backend services such as database, authentication, storage, and real-time subscriptions. This repository demonstrates how to:

1. Set up environment variables for Supabase.
2. Create a Supabase client in Python.
3. Authenticate users.
4. Perform CRUD operations on a "todos" table.

## Prerequisites

- Python installed
- Supabase account and project
- `python-dotenv` and `supabase` Python packages installed
- Environment variables set up in a `.env` file

## Setup

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

## Step 2: Install Dependencies
pip install python-dotenv supabase

Step 3: Configure Environment Variables
Create a .env file in the root of your project directory and add your Supabase URL and Key:
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
