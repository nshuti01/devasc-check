# Devasc_Skills

# 1. GitHub 

Preparation: Ik heb eerst een repository aangemaakt op GitHub.com, hierna zoals in de afbeelding heb ik de GitHub repo in mijn Devasc VM geimporteerd

Implementation:

![image](https://user-images.githubusercontent.com/55875023/149900768-38d2d3d8-ccf0-48ef-bcb1-2eade31c4796.png)

Troubleshooting: Sudo is hier van belang.

Verification:

![image](https://user-images.githubusercontent.com/55875023/149903799-00fa8108-63ce-4070-87d1-41f729ff7725.png)


# 2. Ansible

Preparation: Klaar maken van de Csr100v virtuele router/

Implementation:

![image](https://user-images.githubusercontent.com/55875023/149907914-5080c0e9-0213-4c6c-8a39-6b247d6d4192.png)

![image](https://user-images.githubusercontent.com/55875023/149911670-e568ad41-979d-4d5e-943d-7231aeeb0f12.png)

Troubleshooting: Sinds dat ik direct in mijn GitHub repo bezig ben, moest VS code in sudo gerunned worden, ik heb deze commando gebruikt: sudo code --user-data-dir="~/.vscode-root"

Verification:

![image](https://user-images.githubusercontent.com/55875023/149907637-388653ac-802d-4e97-a53d-06b8e8107d4e.png)

![image](https://user-images.githubusercontent.com/55875023/149911730-5cb04482-e981-4acb-9532-05181d2f42ea.png)

![image](https://user-images.githubusercontent.com/55875023/149911837-06c0a690-ea67-4732-90f9-54c333a69340.png)


# 3. Docker

Preparation: Begrijpen van de Ansible-playbook.

Implementation:

![image](https://user-images.githubusercontent.com/55875023/149919284-f19b3a59-b8b7-407b-a915-77756f3428f3.png)
Rewrite is default inbegrepen in httpd.

![image](https://user-images.githubusercontent.com/55875023/149916940-a0f5a8a2-b4f0-48ec-89f3-d064bb043344.png)
Zoals gevraagd in localhost zal het op poort 8088 runnen.

![image](https://user-images.githubusercontent.com/55875023/149917068-2f4ed7d1-ffe2-4860-af77-c87e57981176.png)

Bash script:
![image](https://user-images.githubusercontent.com/55875023/149928968-b5047848-92c4-4b18-bfd0-3805869a32d1.png)


Troubleshooting: HTML importeren ging niet door foute copy uit te voeren. 
Foute manier: COPY files/index.html /var/www/html/index.html
Correcte manier: COPY files/index.html /usr/local/apache2/htdocs/

Verification:

![image](https://user-images.githubusercontent.com/55875023/149919559-42e50915-0bb3-4b14-a398-e5ed86bca502.png)

# 6. Webex-Teams API

Preparation: Alle nodige scripts bijnemen + API Token genereren.

Implementation:

![image](https://user-images.githubusercontent.com/55875023/149923600-50468c3e-e3a8-41aa-945d-46dc127cc861.png)

![image](https://user-images.githubusercontent.com/55875023/149923641-2a792a83-0597-4f9b-83e2-ccd8fc7890cd.png)

![image](https://user-images.githubusercontent.com/55875023/149923665-5ac2886f-6400-4c4f-b272-f73cd35f8a3f.png)

![image](https://user-images.githubusercontent.com/55875023/149923680-e4ac433f-9532-4a8a-9da9-5513b4625e71.png)

Troubleshooting: Foute invulling van Room_id ...

Verification: 

![image](https://user-images.githubusercontent.com/55875023/149923812-d0eb3a89-9316-41e2-b2c9-93cf691f7788.png)


# 7. Bash

Preparation: CSR100v router opstarten en loopback199 aanmaken.

Implementation:

![image](https://user-images.githubusercontent.com/55875023/149937451-c1bd6454-106d-43ae-8cd6-696a018b928c.png)

Troubleshooting: Ik kan het interface pingen, maar heb een status code 000.

Verification: Gefaald

![image](https://user-images.githubusercontent.com/55875023/149939005-9ccd7493-50ea-4fd5-9d27-77ef48909d06.png)


# 10. Filtering DNAC Response Data

Preparation: Copieren van de script uit de opgave.

Implementation:

![image](https://user-images.githubusercontent.com/55875023/149925169-66c873c2-7e70-4f87-b87c-213c6a8d5d9d.png)

Troubleshooting: Vinden van de juiste parameters. 

Verification: 

![image](https://user-images.githubusercontent.com/55875023/149925242-818c541d-a12e-4904-9016-4c3262d45d9c.png)



