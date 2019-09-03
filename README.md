About
----
Ansible role and zabbix template for Greenplum Database  monitoring.
Compatible with Greenplum 5.

Setup
----
1. Fill gpdb hosts in hosts-prod
2. Fill zabbix info in ansible/vars
3. Setup local environment 
```
source setenv.sh
```
4. Apply ansible
```
ansible-playbook -i hosts-prod greenplum.yml -l gpdb-hosts
```
5. Replace database name in zabbix template
```
sed s/DATABASE/my_db/g -i zbx_export_templates.xml
```
6. Import zbx_export_templates.xml to Zabbix
7. Assign imported template to gpdb hosts


Licence
----
GNU GPL
