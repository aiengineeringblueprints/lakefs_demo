# Testrepo for Lakefs initialization including MinIO S3 Storage

## 0. Start Lakefs, MinIO and Postgres on Fileserver
docker compose up

## 1. Install and setup lakectl, lakectl local and minIO Client

### MinIO
- MinIO Client installieren
    ```
    curl -O https://dl.min.io/client/mc/release/linux-amd64/mc 
    chmod +x mc 
    sudo mv mc /usr/local/bin/
    ```
- `mc alias set localminio http://127.0.0.1:9000 minioadmin minioadmin`
- `mc alias set lakefs http://127.0.0.1:8000 AKIAISFOLKFSSAMPLES wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`
- Überprüfen: `mc alias list`

### LakeCtl
- LakeCtl Client installieren
    ```
    wget https://github.com/treeverse/lakeFS/releases/download/v1.49.1/lakeFS_1.49.1_Linux_x86_64.tar.gz
    tar xfvz lakeFS_1.49.1_Linux_x86_64.tar.gz
	chmod +x lake*
    sudo cp lake* /usr/local/bin/
    ```
- Konfiguration von Lakectl `lakectl config`
    - Acces Key: `AKIAISFOLKFSSAMPLES`
    - Secure Key: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`
    - URL: `http://127.0.0.1:8000/api/v`
- Testen: `lakectl repo list`

## 2. Setup MinIO Bucket, LakeFS Repo and upload data: 
1. MinIO Bucket erstellen (`mc mb localminio/bucket-name`)
2. LakeFS Repository erstellen (`lakectl repo create lakefs://repo-name s3://bucket-name`)
3. Daten uploaden: `mc cp /path/to/data/folder/ lakefs/repo-name/main/data --recursive`
4. Commit data: `lakectl commit lakefs://repo-name/main -m "Upload data"`
Note: Terminal muss im Ordner sein in dem das Repo erstellt wurde (?)

## 3. Usage (lakefs local siehe: https://docs.lakefs.io/quickstart/work-with-data-locally.html)
1. Create Branch: `lakectl branch create lakefs://repo-name/dev --source lakefs://repo-name/main`
2. minio in DNS hinzufügen (um Fehler bei der DNS Auflösung zu vermeiden) `sudo nano /etc/hosts` --> Zeile hinzufügen für `121.0.0.0 minio`
3. Git Repo erstellen (falls der Ordner nicht gecloned wurde): `git init`
3. Clone Data to local folder, Note: The Project must be git tracked! `lakectl local clone lakefs://repo-name/dev/data/ data`
4. ... process_data.py
5. `lakectl local status data`
6. `lakectl local commit -m "resizing all data" data`
7. `lakectl merge lakefs://capsule-endoscopy/nicodev/ lakefs://capsule-endoscopy/main`