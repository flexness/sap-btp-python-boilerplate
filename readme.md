# btp python webapp boilerplate
- boilerplate based on https://developers.sap.com/tutorials/btp-cf-buildpacks-python-create.html

## core
- minimal example routes
- user auth using btp/ias
- role based Access (e.g. for routes, Content)
- Access btp Service (eg hana)
- Access on premise oauth e.g. via principal Propagation?
- Status/ping route

## optional for later
- /routes folder and single py files for every route
- 

## sap tech overview

## cli
- `cf create-service xsuaa application my-xsuaa -c xs-security.json`
- `cf create-service hana hdi-shared my-hana
- `cf push` 
