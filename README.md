[![Hourly Cloud Health Check](https://github.com/FakhrulNabil/cloud-sentinel-python/actions/workflows/cloud_run.yml/badge.svg)](https://github.com/FakhrulNabil/cloud-sentinel-python/actions/workflows/cloud_run.yml)

# Cloud-Sentinel: Automated Python Health Monitor

## ☁️ Cloud Strategy
This project demonstrates a **Serverless Monitoring Solution**. Instead of maintaining a 24/7 server, I am using **GitHub Actions** to spin up an ephemeral Ubuntu instance every hour to verify system uptime.

## 🛠️ Tech Stack
* **Language:** Python 3.9
* **Infrastructure:** GitHub Actions (CI/CD)
* **OS:** Ubuntu Linux (Virtual Machine)
* **Automation:** Cron Scheduling

## 🚀 Key Features
* **Automated Scheduling:** Runs every hour using Cron syntax.
* **Error Reporting:** Returns non-zero exit codes on failure to trigger Cloud alerts.
* **Artifact Logging:** Saves health logs for post-deployment analysis.
