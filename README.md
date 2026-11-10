# security-testbed

> **Warnung: Dieses Repository ist absichtlich verwundbar. Nicht deployen, nicht als Vorlage verwenden, keine Werte daraus übernehmen.**

Das Repository dient als Testobjekt für einen Vergleich automatisierter Absicherungslösungen für Software-Repositories im Rahmen einer Praxisarbeit. Es enthält eine kleine Flask-Anwendung (Python 3.12) sowie Container-, Terraform- und Kubernetes-Dateien.

Alle Zugangsdaten in diesem Repository sind erfunden. Sie gewähren keinen Zugang zu irgendeinem System.

## Aufbau

```text
app/        Flask-Anwendung
deploy/     Bereitstellung
docker/     Dockerfile
infra/      Terraform (Azure)
k8s/        Kubernetes-Manifest
```

Stand: `v1.0`
