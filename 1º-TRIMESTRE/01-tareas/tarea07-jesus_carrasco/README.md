### Enunciado ###
SCSS inicial:
```scss
$bg-color: #df0174;
$size: 1em;
body {
  background-color: $bg-color;
  margin: $size * 4;
}
```

### Comando ejecutado ###
```bash
sass input.scss output.css
```

### Resultado compilado ###
CSS generado:
```css
body {
  background-color: #df0174;
  margin: 4em;
}
```

### Explicación ###
1. **Definición de variables SCSS**:
   - `$bg-color` y `$size` se definen como variables SCSS para almacenar valores reutilizables.
   - `$bg-color: #df0174;` define el color de fondo.
   - `$size: 1em;` define un tamaño base, que se multiplica por `4` al calcular el margen.

2. **Uso de variables**:
   - En el bloque `body`, `background-color` utiliza `$bg-color` como valor.
   - `margin` utiliza `$size` multiplicado por `4`, resultando en `4em`.

3. **Compilación SCSS a CSS**:
   - Al ejecutar el comando `sass`, el preprocesador SCSS transforma el código SCSS en CSS plano, expandiendo las variables y evaluando las expresiones.

4. **Resultado final**:
   - El CSS resultante es funcional y directo, ya que SCSS realiza todas las evaluaciones y el navegador solo interpreta CSS.

### Fichero final ###
El documento generado está adjunto en formato PDF y CSS según lo solicitado.
