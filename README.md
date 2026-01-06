# 🚀 DevSecOps CI/CD Pipeline Lab

## 📌 Visão Geral

Este projeto demonstra, de forma prática, a implementação de uma **pipeline DevSecOps** com foco em **segurança desde o início do ciclo de desenvolvimento (Shift Left Security)**.

Foi utilizada uma **aplicação propositalmente vulnerável** para validar a eficácia de controles de segurança automatizados integrados ao processo de **CI/CD**, evidenciando como vulnerabilidades podem ser **detectadas e bloqueadas antes do deploy**.

O objetivo principal é demonstrar **conhecimento técnico aplicado** em DevSecOps, segurança em pipelines e **gestão de vulnerabilidades**, seguindo práticas adotadas em ambientes corporativos modernos.

---

## 🎯 Objetivos do Projeto

- Implementar uma pipeline CI/CD com **segurança integrada**
- Automatizar a detecção de vulnerabilidades em múltiplas camadas
- Bloquear automaticamente o deploy em caso de riscos críticos
- Demonstrar conceitos de **OWASP Top 10, CWE, CVE e CVSS**
- Evidenciar a aplicação prática de **DevSecOps e Shift Left Security**

---

## 🏗️ Arquitetura da Solução

```text
Developer Commit
        ↓
GitHub Repository
        ↓
GitHub Actions (CI/CD Pipeline)
        ↓
Security Scans (SAST, SCA, Secrets, Container)
        ↓
Pipeline Approval / Block
