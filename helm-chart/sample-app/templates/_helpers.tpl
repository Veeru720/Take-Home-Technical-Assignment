
{{- define "sample-app.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "sample-app.fullname" -}}
{{- printf "%s-%s" (include "sample-app.name" .) .Release.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "sample-app.secretName" -}}
{{- printf "%s-secret" (include "sample-app.name" .) -}}
{{- end -}}
