import api
import ui

datos_usuario = ui.obtener_datos_usuario()
datos_api = api.consultar_api(datos_usuario[0],datos_usuario[1])
datos_df = api.covertir_a_dataframe(datos_api)
ui.mostrar_datos(datos_df)