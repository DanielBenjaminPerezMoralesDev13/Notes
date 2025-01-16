<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/DanielBenjaminPerezMoralesDev13 -->
<!-- Gitlab: https://gitlab.com/DanielBenjaminPerezMoralesDev13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***~/.config/tmux/tmux.conf***

> [!IMPORTANT]
> **Mi configuración de **tmux** se basa en una serie de plugins y configuraciones avanzadas que mejoran la funcionalidad y la experiencia de usuario. A continuación, te explico cada uno de los repositorios en los que te basaste:**

1. **[tmux-plugins/list](https://github.com/tmux-plugins/list "https://github.com/tmux-plugins/list")**
   - *Este repositorio es un índice de todos los plugins disponibles para **tmux** desarrollados por la comunidad y organizados por el equipo de **tmux-plugins**. Contiene una lista completa de plugins que agregan funcionalidades adicionales a **tmux**, como manejo avanzado de ventanas, atajos de teclado, y mucho más.*

2. **[tmux-plugins/tpm](https://github.com/tmux-plugins/tpm "https://github.com/tmux-plugins/tpm")**
   - **TPM (Tmux Plugin Manager)** *es el administrador de plugins para **tmux**. Te permite instalar, actualizar, y eliminar plugins de **tmux** fácilmente. TPM es el núcleo de la gestión de plugins, haciendo que la instalación y mantenimiento de tu entorno **tmux** sea sencillo y automatizado.*

3. **[tmux-plugins/tmux-sensible](https://github.com/tmux-plugins/tmux-sensible "https://github.com/tmux-plugins/tmux-sensible")**
   - *Este plugin ofrece una serie de configuraciones por defecto que hacen que **tmux** sea más intuitivo y fácil de usar. **tmux-sensible** aplica ajustes recomendados para mejorar la usabilidad sin necesidad de configuraciones complejas. Es ideal para usuarios que buscan una configuración optimizada sin muchos ajustes manuales.*

4. **[tmux-plugins/tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect "https://github.com/tmux-plugins/tmux-resurrect")**
   - **tmux-resurrect** *permite guardar y restaurar sesiones de **tmux**. Al usar este plugin, puedes cerrar **tmux** y luego restaurar tu sesión tal como estaba, incluyendo ventanas, paneles, y el contenido en ellos. Es extremadamente útil para mantener tu entorno de trabajo persistente.*

5. **[tmux-plugins/tmux-continuum](https://github.com/tmux-plugins/tmux-continuum "https://github.com/tmux-plugins/tmux-continuum")**
   - **tmux-continuum** *complementa a **tmux-resurrect** al ofrecer salvado automático de sesiones a intervalos regulares y arranque automático de **tmux** al iniciar tu sistema. Este plugin asegura que nunca pierdas tu trabajo y que tu entorno de **tmux** esté siempre listo al encender tu computadora.*

6. **[christoomey/vim-tmux-navigator](https://github.com/christoomey/vim-tmux-navigator "https://github.com/christoomey/vim-tmux-navigator")**
   - *Este plugin permite una integración fluida entre **Vim** y **tmux**. Facilita la navegación entre los splits de **Vim** y los paneles de **tmux** usando las mismas combinaciones de teclas. Es ideal para usuarios de **Vim** que buscan un flujo de trabajo sin interrupciones entre su editor y **tmux**.*

7. **[catppuccin/tmux](https://github.com/catppuccin/tmux "https://github.com/catppuccin/tmux")**
   - **catppuccin/tmux** *proporciona un tema estéticamente agradable para **tmux** basado en la paleta de colores de **Catppuccin**. Este plugin es ideal para quienes buscan una apariencia moderna y consistente en su entorno de **tmux**.*

8. **[sainnhe/tmux-fzf](https://github.com/sainnhe/tmux-fzf "https://github.com/sainnhe/tmux-fzf")**
   - **Para utilizar el plugin sainnhe/tmux-fzf, es necesario tener instalado el binario fzf. Puedes encontrar la guía de instalación en el repositorio oficial de fzf. Consulta el README de fzf para obtener instrucciones detalladas sobre cómo instalarlo [fzf](https://github.com/junegunn/fzf?tab=readme-ov-file#installation "https://github.com/junegunn/fzf?tab=readme-ov-file#installation").**

   - *Este plugin integra **fzf**, un potente motor de búsqueda difusa, dentro de **tmux**. Con **tmux-fzf**, puedes buscar entre tus ventanas y paneles de manera rápida y eficiente, mejorando la productividad al moverte entre diferentes partes de tu sesión.*

9. **[gpakosz/.tmux](https://github.com/gpakosz/.tmux "https://github.com/gpakosz/.tmux")**
   - **gpakosz/.tmux** *es una configuración avanzada de **tmux** que incluye numerosas optimizaciones y mejoras en la interfaz de usuario. Esta configuración es popular por su enfoque en la personalización y mejora de la funcionalidad de **tmux**, proporcionando atajos de teclado adicionales, un status bar mejorado, y soporte para múltiples plugins.*

## ***`tmux list-keys` Comandos Básicos***

- `bind-key -T copy-mode C-Space send-keys -X begin-selection`
  - **Acción:** *Inicia la selección en el modo de copia.*
  - **Prefijo:** *`C-Space` (Ctrl+Espacio).*

- `bind-key -T copy-mode C-a send-keys -X start-of-line`
  - **Acción:** *Mueve el cursor al inicio de la línea.*
  - **Prefijo:** *`C-a` (Ctrl+a).*

- `bind-key -T copy-mode C-b send-keys -X cursor-left`
  - **Acción:** *Mueve el cursor a la izquierda.*
  - **Prefijo:** *`C-b` (Ctrl+b).*

- `bind-key -T copy-mode C-c send-keys -X cancel`
  - **Acción:** *Cancela la selección actual.*
  - **Prefijo:** *`C-c` (Ctrl+c).*

- `bind-key -T copy-mode C-e send-keys -X end-of-line`
  - **Acción:** *Mueve el cursor al final de la línea.*
  - **Prefijo:** *`C-e` (Ctrl+e).*

- `bind-key -T copy-mode C-f send-keys -X cursor-right`
  - **Acción:** *Mueve el cursor a la derecha.*
  - **Prefijo:** *`C-f` (Ctrl+f).*

- `bind-key -T copy-mode C-g send-keys -X clear-selection`
  - **Acción:** *Limpia la selección actual.*
  - **Prefijo:** *`C-g` (Ctrl+g).*

- `bind-key -T copy-mode C-k send-keys -X copy-pipe-end-of-line-and-cancel`
  - **Acción:** *Copia desde la posición del cursor hasta el final de la línea y cancela.*
  - **Prefijo:** *`C-k` (Ctrl+k).*

- `bind-key -T copy-mode C-n send-keys -X cursor-down`
  - **Acción:** *Mueve el cursor hacia abajo.*
  - **Prefijo:** *`C-n` (Ctrl+n).*

- `bind-key -T copy-mode C-p send-keys -X cursor-up`
  - **Acción:** *Mueve el cursor hacia arriba.*
  - **Prefijo:** *`C-p` (Ctrl+p).*

- `bind-key -T copy-mode C-r command-prompt -i -I "#{pane_search_string}" -T search -p "(search up)" { send-keys -X search-backward-incremental "%%" }`
  - **Acción:** *Abre una búsqueda incremental hacia atrás.*
  - **Prefijo:** *`C-r` (Ctrl+r).*

- `bind-key -T copy-mode C-s command-prompt -i -I "#{pane_search_string}" -T search -p "(search down)" { send-keys -X search-forward-incremental "%%" }`
  - **Acción:** *Abre una búsqueda incremental hacia adelante.*
  - **Prefijo:** *`C-s` (Ctrl+s).*

- `bind-key -T copy-mode C-v send-keys -X page-down`
  - **Acción:** *Desplaza la pantalla hacia abajo.*
  - **Prefijo:** *`C-v` (Ctrl+v).*

- `bind-key -T copy-mode C-w send-keys -X copy-pipe-and-cancel`
  - **Acción:** *Copia la selección y cancela.*
  - **Prefijo:** *`C-w` (Ctrl+w).*

- `bind-key -T copy-mode Escape send-keys -X cancel`
  - **Acción:** *Cancela la selección actual.*
  - **Prefijo:** *`Escape`.*

- `bind-key -T copy-mode Space send-keys -X page-down`
  - **Acción:** *Desplaza la pantalla hacia abajo.*
  - **Prefijo:** *`Space` (Espacio).*

### ***Comandos para Búsqueda y Navegación***

- `bind-key -T copy-mode , send-keys -X jump-reverse`
  - **Acción:** *Salta a la ocurrencia anterior de la búsqueda.*
  - **Prefijo:** *`,` (coma).*

- `bind-key -T copy-mode \; send-keys -X jump-again`
  - **Acción:** *Salta a la siguiente ocurrencia de la búsqueda.*
  - **Prefijo:** *`\;` (punto y coma).*

- `bind-key -T copy-mode F command-prompt -1 -p "(jump backward)" { send-keys -X jump-backward "%%" }`
  - **Acción:** *Salta hacia atrás una cantidad especificada de líneas.*
  - **Prefijo:** *`F`.*

- `bind-key -T copy-mode N send-keys -X search-reverse`
  - **Acción:** *Busca la ocurrencia anterior del texto buscado.*
  - **Prefijo:** *`N`.*

- `bind-key -T copy-mode P send-keys -X toggle-position`
  - **Acción:** *Alterna la posición del cursor.*
  - **Prefijo:** *`P`.*

- `bind-key -T copy-mode R send-keys -X rectangle-toggle`
  - **Acción:** *Alterna el modo de selección rectangular.*
  - **Prefijo:** *`R`.*

- `bind-key -T copy-mode T command-prompt -1 -p "(jump to backward)" { send-keys -X jump-to-backward "%%" }`
  - **Acción:** *Salta hacia atrás hasta una línea específica.*
  - **Prefijo:** *`T`.*

- `bind-key -T copy-mode X send-keys -X set-mark`
  - **Acción:** *Establece un marcador en la posición actual.*
  - **Prefijo:** *`X`.*

- `bind-key -T copy-mode f command-prompt -1 -p "(jump forward)" { send-keys -X jump-forward "%%" }`
  - **Acción:** *Salta hacia adelante una cantidad especificada de líneas.*
  - **Prefijo:** *`f`.*

- `bind-key -T copy-mode g command-prompt -p "(goto line)" { send-keys -X goto-line "%%" }`
  - **Acción:** *Salta a una línea específica.*
  - **Prefijo:** *`g`.*

- `bind-key -T copy-mode n send-keys -X search-again`
  - **Acción:** *Busca la siguiente ocurrencia del texto buscado.*
  - **Prefijo:** *`n`.*

- `bind-key -T copy-mode q send-keys -X cancel`
  - **Acción:** *Cancela la selección actual.*
  - **Prefijo:** *`q`.*

- `bind-key -T copy-mode r send-keys -X refresh-from-pane`
  - **Acción:** *Actualiza el contenido desde el panel.*
  - **Prefijo:** *`r`.*

- `bind-key -T copy-mode t command-prompt -1 -p "(jump to forward)" { send-keys -X jump-to-forward "%%" }`
  - **Acción:** *Salta hacia adelante hasta una línea específica.*
  - **Prefijo:** *`t`.*

### ***Comandos para el Ratón***

- `bind-key -T copy-mode MouseDown1Pane select-pane`
  - **Acción:** *Selecciona el panel en el que se hizo clic.*
  - **Prefijo:** *`MouseDown1Pane`.*

- `bind-key -T copy-mode MouseDrag1Pane select-pane \; send-keys -X begin-selection`
  - **Acción:** *Selecciona el panel y empieza una selección.*
  - **Prefijo:** *`MouseDrag1Pane`.*

- `bind-key -T copy-mode MouseDragEnd1Pane send-keys -X copy-pipe-and-cancel`
  - **Acción:** *Copia la selección y cancela.*
  - **Prefijo:** *`MouseDragEnd1Pane`.*

- `bind-key -T copy-mode WheelUpPane select-pane \; send-keys -X -N 5 scroll-up`
  - **Acción:** *Desplaza la pantalla hacia arriba.*
  - **Prefijo:** *`WheelUpPane`.*

- `bind-key -T copy-mode WheelDownPane select-pane \; send-keys -X -N 5 scroll-down`
  - **Acción:** *Desplaza la pantalla hacia abajo.*
  - **Prefijo:** *`WheelDownPane`.*

- `bind-key -T copy-mode DoubleClick1Pane select-pane \; send-keys -X select-word \; run-shell -d 0.3 \; send-keys -X copy-pipe-and-cancel`
  - **Acción:** *Selecciona una palabra con doble clic y la copia.*
  - **Prefijo:** *`DoubleClick1Pane`.*

- `bind-key -T copy-mode TripleClick1Pane select-pane \; send-keys -X select-line \; run-shell -d 0.3 \; send-keys -X copy-pipe-and-cancel`
  - **Acción:** *Selecciona una línea con triple clic y la copia.*
  - **Prefijo:** *`TripleClick1Pane`.*

### ***Comandos de Navegación y Selección***

- `bind-key -T copy-mode Home send-keys -X start-of-line`

- **Acción:** *Mueve el cursor al inicio de la línea.*
- **Prefijo:** *`Home`.*

- `bind-key -T copy-mode End send-keys -X end-of-line`
  - **Acción:** *Mueve el cursor al final de la línea.*
  - **Prefijo:** *`End`.*

- `bind-key -T copy-mode PageUp send-keys -X page-up`
  - **Acción:** *Desplaza la pantalla hacia arriba.*
  - **Prefijo:** *`PageUp`.*

- `bind-key -T copy-mode PageDown send-keys -X page-down`
  - **Acción:** *Desplaza la pantalla hacia abajo.*
  - **Prefijo:** *`PageDown`.*

- `bind-key -T copy-mode Up send-keys -X cursor-up`
  - **Acción:** *Mueve el cursor hacia arriba.*
  - **Prefijo:** *`Up`.*

- `bind-key -T copy-mode Down send-keys -X cursor-down`
  - **Acción:** *Mueve el cursor hacia abajo.*
  - **Prefijo:** *`Down`.*

- `bind-key -T copy-mode Left send-keys -X cursor-left`
  - **Acción:** *Mueve el cursor hacia la izquierda.*
  - **Prefijo:** *`Left`.*

- `bind-key -T copy-mode Right send-keys -X cursor-right`
  - **Acción:** *Mueve el cursor hacia la derecha.*
  - **Prefijo:** *`Right`.*

- `bind-key -T copy-mode A send-keys -X cursor-top`
  - **Acción:** *Mueve el cursor al principio del panel.*
  - **Prefijo:** *`A`.*

- `bind-key -T copy-mode B send-keys -X cursor-bottom`
  - **Acción:** *Mueve el cursor al final del panel.*
  - **Prefijo:** *`B`.*

#### ***Comandos de `tmux`***

1. **`last-pane`**
   - **Acción:** *Cambia al último panel activo en el que estuviste antes del actual. Es útil para alternar rápidamente entre dos paneles.*
   - **Uso:** *`last-pane`*

2. **`last-window`**
   - **Acción:** *Cambia a la última ventana activa en la que estuviste antes de la ventana actual. Esto facilita la navegación entre ventanas.*
   - **Uso:** *`last-window`*

3. **`link-window`**
   - **Acción:** *Permite vincular una ventana existente de una sesión a otra sesión. Esto significa que la misma ventana puede aparecer en múltiples sesiones.*
   - **Uso:** *`link-window -s <session>:<window> -t <target-session>`*

4. **`list-buffers`**
   - **Acción:** *Muestra una lista de todos los buffers de tmux. Los buffers en tmux son áreas de memoria donde se puede copiar y almacenar texto.*
   - **Uso:** *`list-buffers`*

5. **`list-clients`**
   - **Acción:** *Muestra una lista de todos los clientes conectados a la sesión tmux actual. Un cliente en tmux es una instancia de una conexión que interactúa con tmux.*
   - **Uso:** *`list-clients`*

6. **`list-commands`**
   - **Acción:** *Muestra una lista de todos los comandos disponibles en tmux, junto con una breve descripción de cada uno.*
   - **Uso:** *`list-commands`*

7. **`list-keys`**
   - **Acción:** *Muestra una lista de todas las combinaciones de teclas y comandos que están asignados en tmux. Esto te ayuda a ver qué comandos están asociados con qué atajos de teclado.*
   - **Uso:** *`list-keys`*

8. **`list-panes`**
   - **Acción:** *Muestra una lista de todos los paneles en la ventana actual. Incluye información sobre cada panel, como su número y su tamaño.*
   - **Uso:** *`list-panes`*

9. **`list-sessions`**
   - **Acción:** *Muestra una lista de todas las sesiones tmux existentes. Cada sesión puede contener múltiples ventanas y paneles.*
   - **Uso:** *`list-sessions`*

10. **`list-windows`**
    - **Acción:** *Muestra una lista de todas las ventanas en la sesión actual. Incluye información como el número de ventana y el nombre.*
    - **Uso:** *`list-windows`*

11. **`load-buffer`**
    - **Acción:** *Carga un buffer previamente guardado desde un fichero en el buffer actual de tmux. Esto es útil para restaurar texto copiado que se guardó en un fichero.*
    - **Uso:** *`load-buffer <file>`*

12. **`lock-client`**
    - **Acción:** *Bloquea la interfaz del cliente tmux actual, requiriendo una contraseña para desbloquear. Esto es útil para proteger tu sesión mientras no estás presente.*
    - **Uso:** *`lock-client`*

13. **`lock-server`**
    - **Acción:** *Bloquea el servidor tmux completo, requiriendo una contraseña para desbloquear. Esto bloquea todas las sesiones y clientes del servidor tmux.*
    - **Uso:** *`lock-server`*

14. **`lock-session`**
    - **Acción:** *Bloquea la sesión actual de tmux, requiriendo una contraseña para desbloquear. Solo afecta a la sesión en la que se ejecuta.*
    - **Uso:** *`lock-session`*

### ***Ejemplo de uso de `tmux ls`***

**El comando `tmux ls` muestra una lista de sesiones tmux activas:**

```bash
0: 1 windows (created Sun Aug 25 16:52:25 2024) (attached)
```

- *Esto indica que hay una sesión con el ID `0`, que tiene una ventana (`1 window`). La sesión fue creada el 25 de agosto de 2024 a las 16:52 y está actualmente adjunta (es decir, tienes un cliente conectado a ella).*

*Estos comandos te proporcionan herramientas para gestionar y navegar en tmux de manera más eficiente, tanto a nivel de panes, ventanas y sesiones, como para manejar buffers y clientes.*

#### ***Sintaxis básica de `tmux.conf`***

**El fichero de configuración de `tmux` (`tmux.conf`) utiliza una serie de comandos que controlan las diferentes opciones y comportamientos de `tmux`. La sintaxis básica de los comandos es:**

```bash
set [-g | -s] option value
```

- **`set`:** *Este es el comando principal utilizado para establecer una opción en `tmux`. Básicamente, se usa para configurar una opción global, de sesión o de ventana.*
  
- **`-g`:** *Esta es una bandera que indica que la opción es global (`global`). Significa que la opción que se está configurando se aplica a todas las sesiones y ventanas de `tmux`.*
  
- **`-s`:** *Esta bandera indica que la opción es de sesión (`session`). Esto significa que la configuración se aplica solo a la sesión actual. (No se usa en tu configuración, pero es importante saberlo).*

- **`option`:** *Es el nombre de la opción que estás configurando. Cada opción controla un aspecto específico del comportamiento de `tmux`.*

- **`value`:** *Es el valor que se le asigna a la opción. Este valor puede ser un booleano (`on`/`off`), un número, una cadena, etc., dependiendo de la opción que se esté configurando.*

### ***Configuración Detallada***

#### ***1. `set -g mouse on`***

- **Comando:** *`set`*
- **Flag:** *`-g` (global)*
- **Opción:** *`mouse`*
- **Valor:** *`on`*

**Explicación:** *Este comando habilita el soporte para el ratón en `tmux` a nivel global. Es decir, todas las sesiones y ventanas de `tmux` permitirán el uso del ratón para interactuar con los paneles y ventanas (por ejemplo, seleccionar paneles, hacer clic en la barra de estado, desplazarse usando la rueda del ratón, etc.).*

#### ***2. `setw -g monitor-activity on`***

- **Comando:** *`setw` (abreviatura de `set-window-option`)*
- **Flag:** *`-g` (global)*
- **Opción:** *`monitor-activity`*
- **Valor:** *`on`*

**Explicación:** *Este comando configura la opción `monitor-activity` para que esté activa. `setw` se usa para establecer opciones relacionadas específicamente con las ventanas de `tmux`. Con esta opción activada, `tmux` te notificará si hay actividad (como salida nueva) en una ventana que no estás viendo activamente.*

#### ***3. `setw -g window-status-activity-style none`***

- **Comando:** *`setw` (abreviatura de `set-window-option`)*
- **Flag:** *`-g` (global)*
- **Opción:** *`window-status-activity-style`*
- **Valor:** *`none`*

**Explicación:** *Este comando configura la opción `window-status-activity-style` en `tmux` para que no se aplique ningún estilo especial cuando hay actividad en una ventana. `setw` se usa para establecer opciones relacionadas con las ventanas en `tmux`, y en este caso, se está desactivando cualquier resaltado o cambio de estilo en el nombre de la ventana cuando detecta actividad.*

#### ***4. `set -g status-position top`***

- **Comando:** *`set`*
- **Flag:** *`-g` (global)*
- **Opción:** *`status-position`*
- **Valor:** *`top`*

**Explicación:** *Este comando mueve la barra de estado de `tmux` a la parte superior de la pantalla. La barra de estado normalmente se encuentra en la parte inferior, pero con esta opción configurada, se desplaza a la parte superior. Esto aplica globalmente a todas las sesiones de `tmux`.*

#### ***5. `set -g pane-base-index 1`***

- **Comando:** *`set`*
- **Flag:** *`-g` (global)*
- **Opción:** *`pane-base-index`*
- **Valor:** *`1`*

**Explicación:** *Este comando establece el índice base para los paneles en `1` en lugar de `0`. `tmux` normalmente numera los paneles dentro de una ventana comenzando desde `0`, pero con esta configuración, el primer panel será el `1`. Este ajuste se aplica globalmente.*

#### ***6. `set-window-option -g pane-base-index 1`***

- **Comando:** *`set-window-option`*
- **Flag:** *`-g` (global)*
- **Opción:** *`pane-base-index`*
- **Valor:** *`1`*

**Explicación:** *Similar al comando anterior, pero este se usa para asegurar que la configuración de índice de panel también se aplica a nivel de ventana. `set-window-option` es una forma más explícita de `setw` para configurar opciones de ventana.*

#### ***7. `set-option -g renumber-windows on`***

- **Comando:** *`set-option`*
- **Flag:** *`-g` (global)*
- **Opción:** *`renumber-windows`*
- **Valor:** *`on`*

**Explicación:** *Este comando hace que `tmux` renumere automáticamente las ventanas cuando cierras alguna. Es útil para mantener un orden secuencial en las ventanas sin saltos en la numeració***n. `set-option` es un comando genérico para establecer cualquier opción de `tmux`.***

#### ***8. `set -g history-limit 10000`***

- **Comando:** *`set`*
- **Flag:** *`-g` (global)*
- **Opción:** *`history-limit`*
- **Valor:** *`10000`*

**Explicación:** *Este comando establece el límite de historial de `tmux` en `10000` líneas. Esto significa que puedes desplazarte hacia atrás hasta `10000` líneas en cada ventana, lo cual es útil si necesitas revisar mucha salida anterior.*

#### ***9. `set -g mode-keys vi`***

- **Comando:** *`set`*
- **Flag:** *`-g` (global)*
- **Opción:** *`mode-keys`*
- **Valor:** *`vi`*

**Explicación:** *Este comando cambia el modo de teclas para la navegación en el modo de copia de `tmux` a las teclas de estilo `vi`. Esto es útil para usuarios que están familiarizados con `vi` y prefieren usar sus combinaciones de teclas mientras navegan por el buffer de la pantalla.*

### ***1. Lista de Plugins***

**Los plugins en `tmux` se gestionan con `tpm` (Tmux Plugin Manager). Para configurarlos, se utiliza la sintaxis `set -g @plugin 'plugin_name'`.**

```bash
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'
set -g @plugin 'christoomey/vim-tmux-navigator'
set -g @plugin 'catppuccin/tmux#latest'
set -g @plugin 'sainnhe/tmux-fzf'
```

- **Comando:** *`set`*
- **Flag:** *`-g` (global)*
- **Opción:** *`@plugin`*
- **Valor:** *`'plugin_name'`*

**Explicación:** *Estas líneas agregan plugins a la configuración de `tmux` utilizando `tpm`. Los nombres de los plugins siguen el formato `repositorio/plugin`, donde:*

- **`tmux-plugins/tpm`:** *El gestor de plugins para `tmux`.*
- **`tmux-plugins/tmux-sensible`:** *Un conjunto de configuraciones predeterminadas que mejoran la usabilidad de `tmux`.*
- **`tmux-plugins/tmux-resurrect`:** *Permite guardar y restaurar sesiones de `tmux`.*
- **`tmux-plugins/tmux-continuum`:** *Automatiza la restauración y guarda periódicamente sesiones de `tmux`.*
- **`christoomey/vim-tmux-navigator`:** *Facilita la navegación entre `tmux` y panes de `vim`.*
- **`catppuccin/tmux#latest`:** *Un tema visual para `tmux` basado en el esquema de colores Catppuccin.*
- **`sainnhe/tmux-fzf`:** *Integración de `fzf` con `tmux` para búsqueda rápida.*

### ***2. Configuración de `tmux-continuum` y `tmux-resurrect`***

```bash
set -g @continuum-restore 'on'
set -g @resurrect-capture-pane-contents 'on'
set -g @resurrect-strategy-nvim 'session'
```

- **Comando:** *`set`*
- **Flag:** *`-g` (global)*
- **Opción:** *`@continuum-restore`, `@resurrect-capture-pane-contents`, `@resurrect-strategy-nvim`*
- **Valor:** *`'on'`, `'session'`*

**Explicación:**

- **`@continuum-restore 'on'`:** *Habilita la restauración automática de las sesiones al iniciar `tmux`.*
- **`@resurrect-capture-pane-contents 'on'`:** *Captura el contenido de los paneles para ser restaurados posteriormente.*
- **`@resurrect-strategy-nvim 'session'`:** *Especifica la estrategia de restauración para `neovim`, utilizando sesiones.*

### ***3. Configuración de Catppuccin***

```bash
set -g @catppuccin_flavor 'mocha'
set -g @catppuccin_window_left_separator ""
set -g @catppuccin_window_right_separator ""
set -g @catppuccin_window_middle_separator " █"
set -g @catppuccin_window_number_position "right"
set -g @catppuccin_window_default_fill "number"
set -g @catppuccin_window_default_text "#W"
set -g @catppuccin_window_current_fill "number"
set -g @catppuccin_window_current_text "#W"
set -g @catppuccin_status_modules_right "directory user host session"
set -g @catppuccin_status_left_separator " "
set -g @catppuccin_status_right_separator ""
set -g @catppuccin_status_fill "icon"
set -g @catppuccin_status_connect_separator "no"

# Configuracion Ruta Absoluta
# set -g @catppuccin_directory_text "#{pane_current_path}"

# Configuracion Sustituir $HOME Por ~
# set -g @catppuccin_directory_text "#( echo \#{pane_current_path} | sed \"s|$HOME|~|\" )"

# Configuracion Ruta Relative
set -g @catppuccin_directory_text "#{b:pane_current_path}"
```

- **Comando:** *`set`*
- **Flag:** *`-g` (global)*
- **Opción:** *Varias opciones de configuración de Catppuccin*
- **Valor:** *Varios valores específicos*

**Explicación:**
*Estas opciones configuran el tema Catppuccin en `tmux`. Cada línea ajusta un aspecto visual del tema:*

- **`@catppuccin_flavor 'mocha'`:** *Selecciona el esquema de colores `mocha` dentro de los sabores disponibles en Catppuccin.*
- **`@catppuccin_window_left_separator`, `@catppuccin_window_right_separator`:** *Define los separadores visuales a la izquierda y derecha de las ventanas.*
- **`@catppuccin_window_number_position`:** *Establece la posición del número de ventana en la barra de estado.*
- **`@catppuccin_window_default_fill`, `@catppuccin_window_current_fill`:** *Define el relleno visual de las ventanas en la barra de estado.*
- **`@catppuccin_status_modules_right`:** *Configura los módulos que aparecen a la derecha de la barra de estado.*

### ***Configuración de Ruta Absoluta***

```bash
# Configuracion Ruta Absoluta
set -g @catppuccin_directory_text "#{pane_current_path}"
```

- **Descripción:** *Esta configuración muestra la ruta completa o absoluta del directorio actual en el panel de `tmux`.*
- **Sintaxis:**
  - **`#{pane_current_path}`:** *Este es un marcador de posición en `tmux` que se reemplaza dinámicamente con la ruta absoluta del directorio en el que se encuentra el panel activo.*
- **Ejemplo:** *Si estás en el directorio `/home/user/proyecto`, el valor mostrado será exactamente esa ruta completa.*

### ***Configuración para Sustituir `$HOME` por `~`***

```bash
# Configuracion Sustituir $HOME Por ~
set -g @catppuccin_directory_text "#( echo \#{pane_current_path} | sed \"s|$HOME|~|\" )"
```

- **Descripción:** *Esta configuración transforma la ruta absoluta para que el directorio de inicio (`$HOME`) sea representado por `~`, lo que es una convención común en muchas interfaces de línea de comandos.*
- **Sintaxis:**
  - **`#( echo \#{pane_current_path} | sed \"s|$HOME|~|\" )`:** *Este es un comando de shell que se ejecuta dentro de `tmux`:*
    - **`echo \#{pane_current_path}`:** *Imprime la ruta absoluta del directorio actual.*
    - **`sed \"s|$HOME|~|\"`:** *Usa `sed` para sustituir el valor de `$HOME` por `~`. Aquí, `s|...|...|` es la sintaxis de sustitución en `sed`, donde el primer `...` es el texto a buscar y el segundo `...` es el texto que lo reemplazará.*
- **Ejemplo:** *Si `$HOME` es `/home/user`, una ruta como `/home/user/proyecto` se mostrará como `~/proyecto`.*

### ***Configuración de Ruta Relativa***

```bash
# Configuracion Ruta Relative
set -g @catppuccin_directory_text "#{b:pane_current_path}"
```

- **Descripción:** *Esta configuración muestra la ruta relativa del directorio actual, es decir, la ruta desde el directorio raíz del proyecto o desde la directorio de trabajo actual.*
- **Sintaxis:**
  - **`#{b:pane_current_path}`:** *Aquí `#{b:...}` es un formato especial en `tmux` que convierte una ruta absoluta en una relativa.*
    - **`b:`:** *Esto indica que se debe calcular la ruta relativa.*
    - **`pane_current_path`:** *Es la ruta absoluta del panel actual, que será convertida a relativa.*
- **Ejemplo:** *Si estás en `/home/user/proyecto` y `proyecto` es tu directorio base, entonces se mostrará solo `proyecto`.*

- **Resumen:**

- **`#{pane_current_path}`:** *Muestra la ruta completa (absoluta).*
- **`#( echo \#{pane_current_path} | sed \"s|$HOME|~|\" )`:** *Muestra la ruta completa, pero reemplaza el directorio de inicio con `~`.*
- **`#{b:pane_current_path}`:** *Muestra la ruta relativa desde la raíz del proyecto o la directorio base.*

### ***4. Recarga de Configuración***

```bash
unbind r
bind r source-file ~/.config/tmux/tmux.conf\; display-message "Config reloaded ~/.config/tmux/tmux.conf!"
```

- **Comando:** *`unbind` y `bind`*
- **Tecla:** *`r`*
- **Acción:** *Recarga la configuración de `tmux` y muestra un mensaje.*

**Explicación:**

- **`unbind r`:** *Desvincula cualquier acción previamente asignada a la tecla `r`.*
- **`bind r source-file ~/.config/tmux/tmux.conf\; display-message "Config reloaded ~/.config/tmux/tmux.conf!"`:** *Vuelve a vincular la tecla `r` para que recargue el fichero de configuración de `tmux` y muestre un mensaje de confirmación cuando se realice.*

### ***5. Undercurl***

```bash
set -g default-terminal "${TERM}"
set -as terminal-overrides ',*:Smulx=\E[4::%p1%dm'
set -as terminal-overrides ',*:Setulc=\E[58::2::%p1%{65536}%/%d::%p1%{256}%/%{255}%&%d::%p1%{255}%&%d%;m'
```

- **Comando:** *`set`, `set -as`*
- **Flag:** *`-g` (global)*
- **Opción:** *`default-terminal`, `terminal-overrides`*
- **Valor:** *Varios valores específicos*

**Explicación:**

- **`default-terminal "${TERM}"`:** *Establece el tipo de terminal predeterminado en función de la variable de entorno `TERM`.*
- **`set -as terminal-overrides ',*:Smulx=\E[4::%p1%dm'`:** *Habilita el soporte para undercurl (subrayado ondulado) en `tmux`.*
- **`set -as terminal-overrides ',*:Setulc=\E[58::2::%p1%{65536}%/%d::%p1%{256}%/%{255}%&%d::%p1%{255}%&%d%;m'`:** *Permite establecer colores específicos para el undercurl, que requieren una versión de `tmux` 3.0 o superior.*

### ***6. Inicialización del Plugin Manager***

```bash
setenv -g TMUX_PLUGIN_MANAGER_PATH "$HOME/.tmux/plugins/"
if "test ! -d ~/.tmux/plugins/tpm" \
   "run 'git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm && ~/.tmux/plugins/tpm/bin/install_plugins'"
run -b '~/.tmux/plugins/tpm/tpm'
```

- **Comando:** *`setenv`, `if`, `run`*
- **Flag:** *`-g` (global)*
- **Acción:** *Inicialización de `tpm` y descarga automática si no está presente.*

**Explicación:**

- **`setenv -g TMUX_PLUGIN_MANAGER_PATH "$HOME/.tmux/plugins/"`:** *Establece la ruta del gestor de plugins de `tmux`.*
- **`if "test ! -d ~/.tmux/plugins/tpm" "run 'git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm --depth=1 && ~/.tmux/plugins/tpm/bin/install_plugins'"`:** *Comprueba si el gestor de plugins `tpm` está instalado. Si no lo está, lo clona desde GitHub e instala los plugins configurados.*
- **`run -b '~/.tmux/plugins/tpm/tpm'`:** *Ejecuta `tpm` en segundo plano para cargar los plugins.*

> [!IMPORTANT]
> *Este es seccion en la configuración de **tmux** basado en el repositorio de [gpakosz/.tmux](https://github.com/gpakosz/.tmux "https://github.com/gpakosz/.tmux"). Esta configuración incluye muchas opciones y atajos personalizados para mejorar la experiencia de uso de **tmux**. A continuación, te explico cada sección del fichero:*

### ***Comentario General***

*El siguiente código proviene de un fichero de configuración de `tmux`, específicamente del repositorio de [Gregory Pakosz](https://github.com/gpakosz/.tmux "https://github.com/gpakosz/.tmux"). Este fichero está licenciado bajo dos licencias: WTFPL v2 y MIT, lo que permite su uso libre bajo ciertas condiciones, pero sin garantía alguna.*

### ***Línea de Comentario (Shebang)***

```bash
# : << 'EOF'
```

- **Símbolo:** *`#`*
- **Función:** *Indica que la línea es un comentario.*
- **Comentario especial:** *`: << 'EOF'` es un comando heredoc que se utiliza para crear bloques de comentarios. El contenido entre `<< 'EOF'` y `EOF` se trata como un comentario, y no se ejecuta.*

### ***Información de Licencia***

```bash
# https://github.com/gpakosz/.tmux
# (‑●‑●)> dual licensed under the WTFPL v2 license and the MIT license,
#         without any warranty.
#         Copyright 2012— Gregory Pakosz (@gpakosz).
```

- **Símbolo:** *`#`*
- **Función:** *Comenta las líneas que proveen información sobre la fuente del fichero y su licencia.*
- **Enlace:** *`https://github.com/gpakosz/.tmux` es la URL del repositorio de donde proviene la configuración.*
- **Licencias:** *WTFPL v2 y MIT. Ambas licencias permiten modificar y redistribuir el código, con ciertas condiciones:*
  - **WTFPL v2:** *`"Do What The F*ck You Want To Public License"` es una licencia permisiva con solo dos cláusulas: debes hacer lo que quieras con el código, y debes mantener la licencia intacta en cualquier redistribución.*
  - **MIT License:** *Permite el uso, copia, modificación, fusión, publicación, distribución y sublicencia del software, siempre y cuando se incluya una copia del aviso de derechos de autor y la licencia en todas las copias o partes sustanciales del software.*

### ***Advertencia para No Editar el Fichero***

```bash
# ------------------------------------------------------------------------------
# /!\ DO NOT EDIT THIS FILE
#     instead, override your .local customization file copy, see README.md   /!\
# ------------------------------------------------------------------------------
```

- **Símbolo:** *`#`*
- **Función:** *Comenta líneas que advierten al usuario que no debe editar este fichero directamente.*
- **Advertencia:** *El fichero está diseñado para no ser modificado directamente. Cualquier personalización debe hacerse en un fichero de configuración local (`.local`), tal como se menciona en el fichero `README.md`.*

### ***Sección General***

```bash
# -- general -------------------------------------------------------------------
```

- **Símbolo:** *`#`*
- **Función:** *Marca el inicio de la sección general de configuraciones.*
- **Propósito:** *Este comentario indica que las configuraciones a continuación son de carácter general y afectan aspectos básicos del funcionamiento de `tmux`.*

### ***Comentario de Configuración***

```bash
# Comentar Configuracion
# set -g default-terminal "screen-256color"
```

- **Símbolo:** *`#`*
- **Función:** *Desactiva una línea de configuración comentándola.*
- **Comando Comentado:** *`set -g default-terminal "screen-256color"`*
  - **Explicación:** *Ya fue explicado anteriormente. Se desactiva la configuración para dejar que `tmux` utilice la terminal predeterminada del sistema en lugar de forzar `screen-256color`.*

### ***Comando `setw -g xterm-keys on`***

```bash
setw -g xterm-keys on
```

- **Comando:** *`setw`*
  - **Función:** *`setw` es el comando utilizado para establecer opciones de ventana específicas en `tmux`.*
- **Flag `-g`:** *Indica que esta opción se aplica globalmente a todas las ventanas.*
- **Opción `xterm-keys`:**
  - **Función:** *Esta opción habilita el uso de secuencias de teclas extendidas de `xterm`, permitiendo a `tmux` manejar teclas especiales como `Shift`, `Ctrl`, y `Alt` combinadas con otras teclas.*
- **Valor `on`:**
  - **Función:** *Activa la opción `xterm-keys`.*

### ***Comando `set -s escape-time 10`***

```bash
set -s escape-time 10
```

- **Comando:** *`set`*
  - **Función:** *Configura una opción en `tmux`.*
- **Flag `-s`:** *Este flag indica que la configuración es de tipo `server`, aplicándose a nivel del servidor `tmux`.*
- **Opción `escape-time`:**
  - **Función:** *Define el tiempo (en milisegundos) que `tmux` espera después de recibir una secuencia de escape antes de considerar que el usuario ha terminado de escribir una secuencia de comandos.*
- **Valor `10`:**
  - **Función:** *Establece el tiempo de espera en 10 milisegundos, lo que permite que las secuencias de comandos se ejecuten más rápidamente, haciéndolas más responsivas.*

### ***Comando `set -sg repeat-time 600`***

```bash
set -sg repeat-time 600
```

- **Comando:** *`set`*
  - **Función:** *Configura una opción en `tmux`.*
- **Flags `-sg`:**
  - **`-s`:** *Indica que la opción es de tipo `server`.*
  - **`-g`:** *Aplicación global, afecta a todas las sesiones.*
- **Opción `repeat-time`:**
  - **Función:** *Controla el tiempo (en milisegundos) durante el cual una tecla repetida se considera parte del mismo comando. Esto afecta cómo `tmux` interpreta las teclas repetidas.*
- **Valor `600`:**
  - **Función:** *Establece el tiempo de espera en 600 milisegundos, permitiendo un tiempo más largo para que las teclas repetidas se consideren parte del mismo comando.*

### ***Comando `set -s focus-events on`***

```bash
set -s focus-events on
```

- **Comando:** *`set`*
  - **Función:** *Configura una opción en `tmux`.*
- **Flag `-s`:** *Configura la opción a nivel del servidor `tmux`.*
- **Opción `focus-events`:**
  - **Función:** *Esta opción permite que `tmux` envíe notificaciones a las aplicaciones dentro de un panel cuando dicho panel recibe o pierde el foco.*
- **Valor `on`:**
  - **Función:** *Activa la opción, permitiendo que las aplicaciones dentro de `tmux` respondan a cambios de foco.*

### ***Comando `set -g prefix2 C-a`***

```bash
set -g prefix2 C-a
```

- **Comando:** *`set`*
  - **Función:** *Configura una opción en `tmux`.*
- **Flag `-g`:** *Configuración global, afecta a todas las sesiones.*
- **Opción `prefix2`:**
  - **Función:** *`tmux` permite configurar un segundo prefijo de comandos. Normalmente, el prefijo predeterminado es `C-b` (Ctrl + b). Este comando establece un segundo prefijo.*
- **Valor `C-a`:**
  - **Función:** *Asigna `C-a` (Ctrl + a) como el segundo prefijo, emulando el comportamiento del prefijo en `GNU Screen`.*

### ***Comando `bind C-a send-prefix -2`***

```bash
bind C-a send-prefix -2
```

- **Comando:** *`bind`*
  - **Función:** *Asigna una combinación de teclas a una acción específica en `tmux`.*
- **Opción `C-a`:**
  - **Función:** *Especifica la combinación de teclas que se va a asociar con la acción. En este caso, `C-a` (Ctrl + a).*
- **Comando `send-prefix -2`:**
  - **`send-prefix`:** *Envía la secuencia de prefijo a la ventana o panel activo.*
  - **Flag `-2`:** *Indica que se debe enviar el segundo prefijo (`prefix2`) configurado anteriormente. Esto permite que `C-a` funcione como el prefijo para comandos en `tmux`, como lo haría en `GNU Screen`.*

### ***Comando `set -q -g status-utf8 on`***

```bash
set -q -g status-utf8 on
```

- **Comando:** *`set`*
  - **Función:** *Configura una opción en `tmux`.*
- **Flags `-q -g`:**
  - **`-q`:** *`quiet`, suprime errores si la opción no es reconocida. Esto es útil para compatibilidad con versiones anteriores de `tmux`.*
  - **`-g`:** *Aplicación global, afecta a todas las sesiones.*
- **Opción `status-utf8`:**
  - **Función:** *Configura `tmux` para utilizar UTF-8 en la barra de estado.*
- **Valor `on`:**
  - **Función:** *Activa la opción, permitiendo que la barra de estado muestre correctamente caracteres UTF-8. Esta opción es relevante en versiones de `tmux` anteriores a la 2.2.*

### ***Comando `setw -q -g utf8 on`***

```bash
setw -q -g utf8 on
```

- **Comando:** *`setw`*
  - **Función:** *Configura opciones específicas de la ventana.*
- **Flags `-q -g`:**
  - **`-q`:** *Suprime errores si la opción no es reconocida.*
  - **`-g`:** *Aplicación global a todas las ventanas.*
- **Opción `utf8`:**
  - **Función:** *Configura `tmux` para manejar correctamente caracteres UTF-8 en las ventanas.*
- **Valor `on`:**
  - **Función:** *Activa la opción, asegurando que `tmux` maneje adecuadamente la codificación UTF-8 en los paneles y ventanas.*

### ***Comentario de Configuración `set -g history-limit 5000`***

```bash
# Comentar Configuracion
# set -g history-limit 5000                 # boost history
```

- **Símbolo:** *`#`*
- **Función:** *Desactiva la línea de configuración comentándola.*
- **Comando Comentado:** *`set -g history-limit 5000`*
  - **Opción `history-limit`:**
    - **Función:** *Establece el número máximo de líneas de historial que se pueden almacenar para cada panel en `tmux`.*
  - **Valor `5000`:**
    - **Función:** *Especifica que se deben almacenar hasta 5000 líneas de historial por panel.*
  - **Motivo para Comentar:** *Al comentar esta línea, `tmux` utilizará el valor predeterminado del historial, que es 2000 líneas.*

#### ***Explicacion de comandos no usados `bind e`***

- **Comando:** *`bind`*
  - **Función:** *Asigna una combinación de teclas a una acción específica en `tmux`.*
- **Opción `e`:**
  - **Función:** *Define la combinación de teclas `prefix + e` para activar la acción que sigue. Aquí, `prefix` es normalmente `Ctrl + b` (o `Ctrl + a` si has configurado un segundo prefijo como se mostró antes).*

#### ***Explicacion de comandos no usados `new-window -n "#{TMUX_CONF_LOCAL}"`***

- **Comando:** *`new-window`*
  - **Función:** *Crea una nueva ventana en `tmux`.*
- **Opción `-n "#{TMUX_CONF_LOCAL}"`:**
  - **Función:** *Asigna un nombre a la nueva ventana basado en la variable `#{TMUX_CONF_LOCAL}`. Esta variable representa el fichero de configuración local de `tmux`.*

#### ***Explicacion de comandos no usados `-e EDITOR="$EDITOR"`***

- **Opción `-e EDITOR="$EDITOR"`:**
  - **Función:** *Configura la variable de entorno `EDITOR` para esta ventana. Toma el valor actual de la variable `EDITOR` en el entorno, lo cual especifica qué editor de texto utilizar (como `vim`, `nano`, `emacs`, etc.).*

#### ***Explicacion de comandos no usados `sh -c 'case "${EDITOR:-vim}" in *vim*) ... ;; esac && "$TMUX_PROGRAM" ...'`***

- **Comando:** *`sh -c '...'`*
  - **Función:** *Ejecuta un comando de shell en la nueva ventana de `tmux`.*
- **Estructura `case "${EDITOR:-vim}" in *vim*) ... ;; esac`:**
  - **Función:** *Es un bloque de comandos `case` de shell que determina qué editor usar y cómo configurarlo.*
  - **`${EDITOR:-vim}`:**
    - **Función:** *Usa el editor configurado en `EDITOR` o, si no está definido, utiliza `vim` como valor predeterminado.*
  - **`*vim*) ${EDITOR:-vim} -c ":set syntax=tmux" "$TMUX_CONF_LOCAL";;`:**
    - **Función:** *Si el editor es `vim` (o una variante de `vim`), abre el fichero de configuración local `TMUX_CONF_LOCAL` con el comando `vim` y configura la sintaxis para `tmux` (`:set syntax=tmux`).*
  - **`*) $EDITOR "$TMUX_CONF_LOCAL";;`:**
    - **Función:** *Si se está usando un editor que no sea `vim`, simplemente abre el fichero de configuración con el editor especificado en `EDITOR`.*

#### ***Explicacion de comandos no usados `"$TMUX_PROGRAM" ${TMUX_SOCKET:+-S "$TMUX_SOCKET"} source "$TMUX_CONF"`***

- **Comando:** *`"$TMUX_PROGRAM"`*
  - **Función:** *Ejecuta el programa `tmux` en sí mismo, que está almacenado en la variable `TMUX_PROGRAM`.*
- **Opción `source "$TMUX_CONF"`:**
  - **Función:** *Recarga el fichero de configuración principal de `tmux`, especificado en `TMUX_CONF`, después de que el fichero de configuración local haya sido editado.*
- **`${TMUX_SOCKET:+-S "$TMUX_SOCKET"}`:**
  - **Función:** *Si la variable `TMUX_SOCKET` está definida, añade la opción `-S "$TMUX_SOCKET"`, lo que especifica un socket de `tmux` personalizado. Esto es útil para configuraciones avanzadas donde se utilizan múltiples instancias de `tmux`.*

#### ***Explicacion de comandos no usados `\; display "$TMUX_CONF_LOCAL sourced"`***

- **Comando:** *`display`*
  - **Función:** *Muestra un mensaje en la barra de estado de `tmux`.*
- **Mensaje `"$TMUX_CONF_LOCAL sourced"`:**
  - **Función:** *Informa al usuario que el fichero de configuración local `TMUX_CONF_LOCAL` ha sido recargado exitosamente.*

### ***Explicacion de comandos no usados Comando para Recargar la Configuración***

```bash
bind r run '"$TMUX_PROGRAM" ${TMUX_SOCKET:+-S "$TMUX_SOCKET"} source "$TMUX_CONF"' \; display "#{TMUX_CONF} sourced"
```

#### ***Explicacion de comandos no usados `bind r`***

- **Comando:** *`bind`*
  - **Función:** *Asigna una combinación de teclas a una acción específica en `tmux`.*
- **Opción `r`:**
  - **Función:** *Define la combinación de teclas `prefix + r` para activar la acción que sigue.*

#### ***Explicacion de comandos no usados `run '"$TMUX_PROGRAM" ${TMUX_SOCKET:+-S "$TMUX_SOCKET"} source "$TMUX_CONF"'`***

- **Comando:** *`run`*
  - **Función:** *Ejecuta un comando de shell dentro de `tmux`.*
- **`"$TMUX_PROGRAM" ${TMUX_SOCKET:+-S "$TMUX_SOCKET"} source "$TMUX_CONF"`:**
  - **Función:** *Este comando recarga el fichero de configuración principal `TMUX_CONF` utilizando el programa `tmux`. Como se explicó anteriormente, la parte `${TMUX_SOCKET:+-S "$TMUX_SOCKET"}` especifica un socket de `tmux` personalizado si `TMUX_SOCKET` está definido.*

#### ***Explicacion de comandos no usados `\; display "#{TMUX_CONF} sourced"`***

- **Comando:** *`display`*
  - **Función:** *Muestra un mensaje en la barra de estado de `tmux`.*
- **Mensaje `#{TMUX_CONF} sourced`:**
  - **Función:** *Informa al usuario que el fichero de configuración `TMUX_CONF` ha sido recargado exitosamente.*

> [!NOTE]
> *Estos comandos de `tmux` proporcionan atajos convenientes para editar y recargar la configuración de `tmux` directamente desde una sesión activa. Con `prefix + e`, se abre el fichero de configuración local en una nueva ventana de `tmux` usando el editor de texto preferido. Después de hacer cambios, el fichero de configuración principal se recarga automáticamente, asegurando que las nuevas configuraciones se apliquen de inmediato. Con `prefix + r`, se puede recargar rápidamente el fichero de configuración principal sin necesidad de abrir un editor, aplicando cualquier cambio que se haya hecho directamente en el fichero de configuración.*

### ***Numeración de Ventanas y Paneles***

```bash
set -g base-index 1           # start windows numbering at 1
setw -g pane-base-index 1     # make pane numbering consistent with windows
```

- **Comando `set`:**
  - **Opción `-g`:** *Define una configuración global para toda la sesión de `tmux`.*
  - **`base-index 1`:**
    - **Función:** *Cambia la numeración de las ventanas de `tmux` para que comience desde 1 en lugar de 0. Esto puede ser más intuitivo, especialmente si prefieres que la primera ventana sea numerada como 1.*
  
- **Comando `setw`:**
  - **Opción `-g`:** *Define una configuración global para todos los paneles dentro de la sesión.*
  - **`pane-base-index 1`:**
    - **Función:** *Alinea la numeración de los paneles dentro de una ventana para que comience también en 1. Esto hace que la numeración de los paneles sea consistente con la de las ventanas.*

### ***Renombrado Automático y Reordenación de Ventanas***

```bash
setw -g automatic-rename on   # rename window to reflect current program
set -g renumber-windows on    # renumber windows when a window is closed
```

- **`automatic-rename on`:**
  - **Función:** *Activa el renombrado automático de las ventanas en `tmux` para que reflejen el nombre del programa que se está ejecutando en esa ventana. Por ejemplo, si abres `vim` en una ventana, la ventana podría renombrarse automáticamente a "vim".*
  
- **`renumber-windows on`:**
  - **Función:** *Activa la re-numeración automática de ventanas. Cuando cierras una ventana, las demás ventanas se re-numeran para llenar el hueco dejado por la ventana cerrada, manteniendo una secuencia continua de números de ventanas.*

### ***Configuración del Título del Terminal***

```bash
set -g set-titles on          # set terminal title
```

- **`set-titles on`:**
  - **Función:** *Activa la actualización del título de la ventana del terminal para reflejar la ventana activa de `tmux`. Esto es útil si quieres ver el nombre de la ventana de `tmux` como el título de la ventana de tu terminal.*

### ***Tiempo de Visualización***

```bash
set -g display-panes-time 800 # slightly longer pane indicators display time
set -g display-time 1000      # slightly longer status messages display time
```

- **`display-panes-time 800`:**
  - **Función:** *Configura el tiempo (en milisegundos) que se muestran los indicadores de los paneles cuando se activa la visualización de paneles (`prefix + q`). Aquí, se configura para 800 milisegundos, lo que proporciona un poco más de tiempo para ver los números de los paneles.*

- **`display-time 1000`:**
  - **Función:** *Configura el tiempo (en milisegundos) que se muestran los mensajes de estado en la barra de estado. En este caso, 1000 milisegundos (1 segundo) es el tiempo que los mensajes de estado serán visibles.*

### ***Intervalo de Redibujado de la Barra de Estado***

```bash
# set -g status-interval 10     # redraw status line every 10 seconds
set -g status-interval 1     # redraw status line every 1 seconds
```

- **Comando `set -g status-interval`:**
  - **Función:** *Define la frecuencia con la que se redibuja la línea de estado en `tmux`. Por defecto, se redibuja cada 10 segundos.*
  - **Configuración personalizada:** *Cambiar este valor a 1 segundo significa que la barra de estado se actualizará cada segundo, lo que puede ser útil si tienes información dinámica que quieres que se actualice rápidamente.*

### ***Limpiar Pantalla e Historial***

```bash
# bind -n C-M-l send-keys "clear -T $TERM && tmux clear-history"
bind -n C-M-l send-keys "clear -T $TERM && tmux clear-history"\; send-keys Enter
```

- **`bind -n C-M-l`:**
  - **Función:** *Asigna la combinación de teclas `Ctrl + Alt + l` (representada por `C-M-l`) a una acción específica.*
  - **Opción `-n`:** *Indica que este binding es "sin prefijo", lo que significa que la combinación de teclas se activa sin necesidad de usar el prefijo habitual (`Ctrl + b` o `Ctrl + a`).*

- **`send-keys "clear -T $TERM && tmux clear-history"`:**
  - **Función:** *Envía los comandos `clear -T $TERM` y `tmux clear-history` al terminal.*
  - **`clear -T $TERM`:** *Limpia la pantalla del terminal utilizando el tipo de terminal actual (`$TERM`).*
  - **`tmux clear-history`:** *Limpia el historial de desplazamiento (`scrollback`) del terminal en `tmux`.*
  
- **`send-keys Enter`:**
  - **Función:** *Envía un "Enter" para ejecutar el comando anterior. Esto asegura que el comando de limpieza de pantalla e historial se ejecute inmediatamente.*

### ***Actividad del Panel***

```bash
set -g monitor-activity on
set -g visual-activity on
```

- **`monitor-activity on`:**
  - **Función:** *Activa la monitorización de actividad en los paneles de `tmux`. Si algún panel que no está visible recibe actividad (como la salida de un comando), `tmux` lo notifica.*

- **`visual-activity on`:**
  - **Función:** *Activa las notificaciones visuales para la actividad del panel. Esto significa que, además de monitorizar la actividad, `tmux` mostrará una notificación visual (como un cambio de color en la barra de estado) cuando haya actividad en un panel que no esté actualmente visible.*

- **Esta configuración de `tmux` está diseñada para mejorar la experiencia visual y la usabilidad general:**

- *La numeración de ventanas y paneles comienza en 1 para mayor coherencia.*
- *Las ventanas se renombran automáticamente y se re-numeran al cerrarse, manteniendo la organización.*
- *El título del terminal refleja la ventana activa.*
- *Los tiempos de visualización de los indicadores de paneles y mensajes de estado se extienden ligeramente.*
- *La barra de estado se actualiza cada segundo para mantener la información actualizada.*
- *Se proporciona una combinación de teclas para limpiar rápidamente tanto la pantalla como el historial.*
- *La actividad del panel se monitoriza y se notifica visualmente para asegurar que no se pierda ninguna salida importante.*

### ***-- Navigation ----------------------------------------------------------------***

1. **Crear sesión**
   - `bind C-c new-session`
   - **Descripción:** *Asocia la combinación de teclas `Ctrl-c` para crear una nueva sesión de `tmux`.*

2. **Navegación entre sesiones**
   - `bind BTab switch-client -l`
   - **Descripción:** *Asocia `Ctrl-Tab` para cambiar a la última sesión activa. Esto te permite alternar rápidamente entre dos sesiones.*

3. **División de ventanas**
   - `bind - split-window -v`
   - **Descripción:** *Asocia la tecla `-` para dividir la ventana actual horizontalmente.*
   - `bind _ split-window -h`
   - **Descripción:** *Asocia la tecla `_` para dividir la ventana actual verticalmente.*

4. **Navegación entre paneles**
   - `bind -r h select-pane -L`
   - `bind -r j select-pane -D`
   - `bind -r k select-pane -U`
   - `bind -r l select-pane -R`
   - **Descripción:** *Asocia las teclas `h`, `j`, `k`, y `l` (en modo repetitivo) para navegar entre paneles en las direcciones izquierda, abajo, arriba y derecha, respectivamente.*
   - `bind > swap-pane -D`
   - **Descripción:** *Asocia la tecla `>` para intercambiar el panel actual con el siguiente panel en la ventana.*
   - `bind < swap-pane -U`
   - **Descripción:** *Asocia la tecla `<` para intercambiar el panel actual con el panel anterior en la ventana.*

5. **Redimensionamiento de paneles**
   - `bind -r H resize-pane -L 2`
   - `bind -r J resize-pane -D 2`
   - `bind -r K resize-pane -U 2`
   - `bind -r L resize-pane -R 2`
   - **Descripción:** *Asocia las teclas `H`, `J`, `K`, y `L` (en modo repetitivo) para redimensionar el panel actual en 2 unidades en las direcciones izquierda, abajo, arriba y derecha, respectivamente.*

6. **Navegación entre ventanas**
   - `unbind n`
   - `unbind p`
   - **Descripción:** *Desvincula las teclas `n` y `p` de la navegación entre ventanas.*
   - `bind -r C-h previous-window`
   - **Descripción:** *Asocia `Ctrl-h` para seleccionar la ventana anterior.*
   - `bind -r C-l next-window`
   - **Descripción:** *Asocia `Ctrl-l` para seleccionar la siguiente ventana.*
   - `bind Tab last-window`
   - **Descripción:** *Asocia la tecla `Tab` para cambiar a la última ventana activa.*

### ***-- Copy Mode -----------------------------------------------------------------***

1. **Entrar en el modo de copiar**
   - `bind Enter copy-mode`
   - **Descripción:** *Asocia la tecla `Enter` para entrar en el modo de copiar.*

2. **Acciones en el modo de copiar (modo vi)**
   - `bind -T copy-mode-vi v send -X begin-selection`
   - **Descripción:** *Asocia la tecla `v` en modo de copiar (estilo `vi`) para iniciar la selección de texto.*
   - `bind -T copy-mode-vi C-v send -X rectangle-toggle`
   - **Descripción:** *Asocia `Ctrl-v` para seleccionar un área rectangular de texto.*
   - `bind -T copy-mode-vi y send -X copy-selection-and-cancel`
   - **Descripción:** *Asocia `y` para copiar la selección de texto y cancelar el modo de copiar.*
   - `bind -T copy-mode-vi Escape send -X cancel`
   - **Descripción:** *Asocia `Escape` para cancelar la selección y salir del modo de copiar.*
   - `bind -T copy-mode-vi H send -X start-of-line`
   - **Descripción:** *Asocia `H` para mover el cursor al inicio de la línea actual.*
   - `bind -T copy-mode-vi L send -X end-of-line`
   - **Descripción:** *Asocia `L` para mover el cursor al final de la línea actual.*

### ***-- Buffers -------------------------------------------------------------------***

1. **Gestión de buffers**
   - `bind b list-buffers`
   - **Descripción:** *Asocia la tecla `b` para listar todos los buffers de tmux.*
   - `bind p paste-buffer -p`
   - **Descripción:** *Asocia la tecla `p` para pegar el buffer en la parte superior de la lista de buffers.*
   - `bind P choose-buffer`
   - **Descripción:** *Asocia la tecla `P` para elegir de qué buffer pegar.*

### ***Configuraciones Comentadas***

**Estas configuraciones están comentadas y no se ejecutarán a menos que se descomenten. Aquí está el propósito de cada una:**

1. **Buscar sesión**
   - `# bind C-f command-prompt -p find-session 'switch-client -t %%'`
   - **Descripción:** *Permitir buscar y cambiar a una sesión específica usando `Ctrl-f`.*

2. **Maximizar panel**
   - `# bind + run "cut -c3- '#{TMUX_CONF}' | sh -s _maximize_pane '#{session_name}' '#D'"`
   - **Descripción:** *Maximizar el panel actual. Descomentarlo si necesitas esta funcionalidad.*

3. **Alternar mouse**
   - `# bind m run "cut -c3- '#{TMUX_CONF}' | sh -s _toggle_mouse"`
   - **Descripción:** *Alternar el uso del mouse en `tmux`.*

4. **Pathpicker de Facebook**
   - `# bind F run "cut -c3- '#{TMUX_CONF}' | sh -s _fpp '#{pane_id}' '#{pane_current_path}'"`
   - **Descripción:** *Ejecutar una herramienta específica para gestionar rutas (Pathpicker) usando `F`.*

5. **Copiar al portapapeles (X11, Wayland, macOS, Windows)**
   - *Estas líneas permiten copiar al portapapeles de diferentes sistemas operativos y entornos gráficos (X11, Wayland, macOS, Windows).*

#### ***Configuracion Completa ~/.config/tmux/tmux.conf***

```bash
# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielBenjaminPerezMoralesDev13
# Gitlab: https://gitlab.com/DanielBenjaminPerezMoralesDev13
# Correo electrónico: danielperezdev@proton.me

# ~/.config/tmux/tmux.conf

# Repository Plugins
# Lista de Plugins: https://github.com/tmux-plugins/list
# tpm: https://github.com/tmux-plugins/tpm
# tmux-sensible: https://github.com/tmux-plugins/tmux-sensible
# tmux-resurrect: https://github.com/tmux-plugins/tmux-resurrect
# tmux-continuum: https://github.com/tmux-plugins/tmux-continuum
# vim-tmux-navigator: https://github.com/christoomey/vim-tmux-navigator
# tmux: https://github.com/catppuccin/tmux
# tmux-fzf: https://github.com/sainnhe/tmux-fzf 
# tmux-fzf Requiere binario fzf: https://github.com/junegunn/fzf?tab=readme-ov-file#installation
# .tmux: https://github.com/gpakosz/.tmux

# Configuracion Comentada
# set -g default-terminal "$TERM"

# Configuración básica
set -g mouse on
setw -g monitor-activity on
setw -g window-status-activity-style none
set -g status-position top
set -g pane-base-index 1
set-window-option -g pane-base-index 1
set-option -g renumber-windows on
set -g history-limit 10000
set -g mode-keys vi

# Lista de plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'
set -g @plugin 'christoomey/vim-tmux-navigator'
set -g @plugin 'catppuccin/tmux#latest'
set -g @plugin 'sainnhe/tmux-fzf'

# tmux-continuum & tmux-resurrecrt
set -g @continuum-restore 'on'
set -g @resurrect-capture-pane-contents 'on'
set -g @resurrect-strategy-nvim 'session'

# Configuración de Catppuccin
set -g @catppuccin_flavor 'mocha'
set -g @catppuccin_window_left_separator ""
set -g @catppuccin_window_right_separator ""
set -g @catppuccin_window_middle_separator " █"
set -g @catppuccin_window_number_position "right"
set -g @catppuccin_window_default_fill "number"
set -g @catppuccin_window_default_text "#W"
set -g @catppuccin_window_current_fill "number"
set -g @catppuccin_window_current_text "#W"
set -g @catppuccin_status_modules_right "directory user host session"
set -g @catppuccin_status_left_separator " "
set -g @catppuccin_status_right_separator ""
set -g @catppuccin_status_fill "icon"
set -g @catppuccin_status_connect_separator "no"

# Configuracion Ruta Absoluta
# set -g @catppuccin_directory_text "#{pane_current_path}"

# Configuracion Sustituir $HOME Por ~
# set -g @catppuccin_directory_text "#( echo \#{pane_current_path} | sed \"s|$HOME|~|\" )"

# Configuracion Ruta Relative
set -g @catppuccin_directory_text "#{b:pane_current_path}"

# Recarga de configuración
unbind r
bind r source-file ~/.config/tmux/tmux.conf\; display-message "Config reloaded ~/.config/tmux/tmux.conf!"

# create session
bind C-c new-session

# find session
bind C-f command-prompt -p find-session 'switch-client -t %%'

# session navigation
bind BTab switch-client -l  # move to last session

# split current window horizontally
bind - split-window -v
# split current window vertically
bind _ split-window -h

# pane navigation
bind -r h select-pane -L  # move left
bind -r j select-pane -D  # move down
bind -r k select-pane -U  # move up
bind -r l select-pane -R  # move right
bind > swap-pane -D       # swap current pane with the next one
bind < swap-pane -U       # swap current pane with the previous one

# Configuracion Comentada
# maximize current pane
# bind + run "cut -c3- '#{TMUX_CONF}' | sh -s _maximize_pane '#{session_name}' '#D'"

# pane resizing
bind -r H resize-pane -L 2
bind -r J resize-pane -D 2
bind -r K resize-pane -U 2
bind -r L resize-pane -R 2

# window navigation
unbind n
unbind p
bind -r C-h previous-window # select previous window
bind -r C-l next-window     # select next window
bind Tab last-window        # move to last active window

# Configuración Comentada
# toggle mouse
# bind m run "cut -c3- '#{TMUX_CONF}' | sh -s _toggle_mouse"

# Configuracion Comentada
# -- facebook pathpicker -------------------------------------------------------
# bind F run "cut -c3- '#{TMUX_CONF}' | sh -s _fpp '#{pane_id}' '#{pane_current_path}'"

# Undercurl
set -g default-terminal "${TERM}"
set -as terminal-overrides ',*:Smulx=\E[4::%p1%dm'  # undercurl support
set -as terminal-overrides ',*:Setulc=\E[58::2::%p1%{65536}%/%d::%p1%{256}%/%{255}%&%d::%p1%{255}%&%d%;m'  # underscore colours - needs tmux-3.0

# Inicialización del plugin manager
setenv -g TMUX_PLUGIN_MANAGER_PATH "$HOME/.tmux/plugins/"
if "test ! -d ~/.tmux/plugins/tpm" \
   "run 'git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm --depth=1 && ~/.tmux/plugins/tpm/bin/install_plugins'"
run -b '~/.tmux/plugins/tpm/tpm'

# : << 'EOF'
# https://github.com/gpakosz/.tmux
# (‑●‑●)> dual licensed under the WTFPL v2 license and the MIT license,
#         without any warranty.
#         Copyright 2012— Gregory Pakosz (@gpakosz).
#
# ------------------------------------------------------------------------------
# /!\ DO NOT EDIT THIS FILE
#     instead, override your .local customization file copy, see README.md   /!\
# ------------------------------------------------------------------------------


# -- general -------------------------------------------------------------------

# Comentar Configuracion
# set -g default-terminal "screen-256color"

setw -g xterm-keys on
set -s escape-time 10                     # faster command sequences
set -sg repeat-time 600                   # increase repeat timeout
set -s focus-events on

set -g prefix2 C-a                        # GNU-Screen compatible prefix
bind C-a send-prefix -2

set -q -g status-utf8 on                  # expect UTF-8 (tmux < 2.2)
setw -q -g utf8 on

# Comentar Configuracion
# set -g history-limit 5000                 # boost history

# Comentar Configuracion
# edit configuration
# bind e new-window -n "#{TMUX_CONF_LOCAL}" -e EDITOR="$EDITOR" sh -c 'case "${EDITOR:-vim}" in *vim*) ${EDITOR:-vim} -c ":set syntax=tmux" "$TMUX_CONF_LOCAL";; *) $EDITOR "$TMUX_CONF_LOCAL";; esac && "$TMUX_PROGRAM" ${TMUX_SOCKET:+-S "$TMUX_SOCKET"} source "$TMUX_CONF" \; display "$TMUX_CONF_LOCAL sourced"'

# Comentar Configuracion
# reload configuration
# bind r run '"$TMUX_PROGRAM" ${TMUX_SOCKET:+-S "$TMUX_SOCKET"} source "$TMUX_CONF"' \; display "#{TMUX_CONF} sourced"


# -- display -------------------------------------------------------------------

set -g base-index 1           # start windows numbering at 1
setw -g pane-base-index 1     # make pane numbering consistent with windows

setw -g automatic-rename on   # rename window to reflect current program
set -g renumber-windows on    # renumber windows when a window is closed

set -g set-titles on          # set terminal title

set -g display-panes-time 800 # slightly longer pane indicators display time
set -g display-time 1000      # slightly longer status messages display time

# Configuracion Default
# set -g status-interval 10     # redraw status line every 10 seconds

# Actualizar la barra de estado cada 1 segundo
set -g status-interval 1     # redraw status line every 1 seconds


# clear both screen and history
# Dejar Ctrl + L para ir a la derecha (vim-tmux-navigator)

# Opcional
# bind -n C-M-l send-keys "clear -T $TERM && tmux clear-history"

# Configuracion Recomendada
bind -n C-M-l send-keys "clear -T $TERM && tmux clear-history"\; send-keys Enter

# Configuracion Default
# bind -n C-l send-keys C-l \; run 'sleep 0.2' \; clear-history

# activity
set -g monitor-activity on

# Configuracion Default
# set -g visual-activity off

# Configuracion Recomendada
set -g visual-activity on


# -- navigation ----------------------------------------------------------------

# create session
bind C-c new-session

# Configuracion Comentada
# find session
# bind C-f command-prompt -p find-session 'switch-client -t %%'

# session navigation
bind BTab switch-client -l  # move to last session

# split current window horizontally
bind - split-window -v
# split current window vertically
bind _ split-window -h

# pane navigation
bind -r h select-pane -L  # move left
bind -r j select-pane -D  # move down
bind -r k select-pane -U  # move up
bind -r l select-pane -R  # move right
bind > swap-pane -D       # swap current pane with the next one
bind < swap-pane -U       # swap current pane with the previous one

# Configuracion Comentada
# maximize current pane
# bind + run "cut -c3- '#{TMUX_CONF}' | sh -s _maximize_pane '#{session_name}' '#D'"

# pane resizing
bind -r H resize-pane -L 2
bind -r J resize-pane -D 2
bind -r K resize-pane -U 2
bind -r L resize-pane -R 2

# window navigation
unbind n
unbind p
bind -r C-h previous-window # select previous window
bind -r C-l next-window     # select next window
bind Tab last-window        # move to last active window

# Configuración Comentada
# toggle mouse
# bind m run "cut -c3- '#{TMUX_CONF}' | sh -s _toggle_mouse"

# Configuracion Comentada
# -- facebook pathpicker -------------------------------------------------------
# bind F run "cut -c3- '#{TMUX_CONF}' | sh -s _fpp '#{pane_id}' '#{pane_current_path}'"


# -- copy mode -----------------------------------------------------------------

bind Enter copy-mode # enter copy mode

bind -T copy-mode-vi v send -X begin-selection
bind -T copy-mode-vi C-v send -X rectangle-toggle
bind -T copy-mode-vi y send -X copy-selection-and-cancel
bind -T copy-mode-vi Escape send -X cancel
bind -T copy-mode-vi H send -X start-of-line
bind -T copy-mode-vi L send -X end-of-line

# copy to X11 clipboard
# if -b 'command -v xsel > /dev/null 2>&1' 'bind y run -b "\"\$TMUX_PROGRAM\" \${TMUX_SOCKET:+-S \"\$TMUX_SOCKET\"} save-buffer - | xsel -i -b"'
# if -b '! command -v xsel > /dev/null 2>&1 && command -v xclip > /dev/null 2>&1' 'bind y run -b "\"\$TMUX_PROGRAM\" \${TMUX_SOCKET:+-S \"\$TMUX_SOCKET\"} save-buffer - | xclip -i -selection clipboard >/dev/null 2>&1"'
# # copy to Wayland clipboard
# if -b '[ "$XDG_SESSION_TYPE" = "wayland" ] && command -v wl-copy > /dev/null 2>&1' 'bind y run -b "\"\$TMUX_PROGRAM\" \${TMUX_SOCKET:+-S \"\$TMUX_SOCKET\"} save-buffer - | wl-copy"'
# # copy to macOS clipboard
# if -b 'command -v pbcopy > /dev/null 2>&1' 'bind y run -b "\"\$TMUX_PROGRAM\" \${TMUX_SOCKET:+-S \"\$TMUX_SOCKET\"} save-buffer - | pbcopy"'
# # copy to Windows clipboard
# if -b 'command -v clip.exe > /dev/null 2>&1' 'bind y run -b "\"\$TMUX_PROGRAM\" \${TMUX_SOCKET:+-S \"\$TMUX_SOCKET\"} save-buffer - | clip.exe"'
# if -b '[ -c /dev/clipboard ]' 'bind y run -b "\"\$TMUX_PROGRAM\" \${TMUX_SOCKET:+-S \"\$TMUX_SOCKET\"} save-buffer - > /dev/clipboard"'


# -- buffers -------------------------------------------------------------------

bind b list-buffers     # list paste buffers
bind p paste-buffer -p  # paste from the top paste buffer
bind P choose-buffer    # choose which buffer to paste from


# -- 8< ------------------------------------------------------------------------
# Configuracion Comentada
# %if #{==:#{TMUX_PROGRAM},}
#   run 'TMUX_PROGRAM="$(LSOF=$(PATH="$PATH:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin" command -v lsof); $LSOF -b -w -a -d txt -p #{pid} -Fn 2>/dev/null | perl -n -e "if (s/^n((?:.(?!dylib$|so$))+)$/\1/g && s/(?:\s+\([^\s]+?\))?$//g) { print; exit } } exit 1; {" || readlink "/proc/#{pid}/exe" 2>/dev/null)"; {[ -f "$TMUX_PROGRAM" ] && [ -x "$TMUX_PROGRAM" ]} || TMUX_PROGRAM="$(command -v tmux || printf tmux)"; "$TMUX_PROGRAM" -S #{socket_path} set-environment -g TMUX_PROGRAM "$TMUX_PROGRAM"'
# %endif
# %if #{==:#{TMUX_SOCKET},}
#   run '"$TMUX_PROGRAM" -S #{socket_path} set-environment -g TMUX_SOCKET "#{socket_path}"'
# %endif
# %if #{==:#{TMUX_CONF},}
#   run '"$TMUX_PROGRAM" set-environment -g TMUX_CONF $(for conf in "$HOME/.tmux.conf" "$XDG_CONFIG_HOME/tmux/tmux.conf" "$HOME/.config/tmux/tmux.conf"; do [ -f "$conf" ] && printf "%s" "$conf" && break; done)'
# %endif
# %if #{==:#{TMUX_CONF_LOCAL},}
#   run '"$TMUX_PROGRAM" set-environment -g TMUX_CONF_LOCAL "$TMUX_CONF.local"'
# %endif


# Configuración Comentada
# run '"$TMUX_PROGRAM" source "$TMUX_CONF_LOCAL"'
# run 'cut -c3- "$TMUX_CONF" | sh -s _apply_configuration'


# EOF
#
# # exit the script if any statement returns a non-true return value
# set -e
#
# unset GREP_OPTIONS
# export LC_NUMERIC=C
# # shellcheck disable=SC3041
# if (set +H 2>/dev/null); then
#   set +H
# fi
#
# if ! printf '' | sed -E 's///' 2>/dev/null; then
#   if printf '' | sed -r 's///' 2>/dev/null; then
#     sed() {
#       n=$#; while [ "$n" -gt 0 ]; do arg=$1; shift; case $arg in -E*) arg=-r${arg#-E};; esac; set -- "$@" "$arg"; n=$(( n - 1 )); done
#       command sed "$@"
#     }
#   fi
# fi
#
# _uname_s=$(uname -s)
#
# [ -z "$TMUX" ] && exit 255
# if [ -z "$TMUX_SOCKET" ]; then
#   TMUX_SOCKET=$(printf '%s' "$TMUX" | cut -d, -f1)
# fi
# if [ -z "$TMUX_PROGRAM" ]; then
#   TMUX_PID=$(printf '%s' "$TMUX" | cut -d, -f2)
#   TMUX_PROGRAM=$(lsof -b -w -a -d txt -p "$TMUX_PID" -Fn 2>/dev/null | perl -n -e "if (s/^n((?:.(?!dylib$|so$))+)$/\1/g) { print; exit } } exit 1; {" || readlink "/proc/$TMUX_PID/exe" 2>/dev/null || printf tmux)
# fi
# if [ "$TMUX_PROGRAM" = "tmux" ]; then
#   tmux() {
#     command tmux ${TMUX_SOCKET:+-S "$TMUX_SOCKET"} "$@"
#   }
# else
#   tmux() {
#     "$TMUX_PROGRAM" ${TMUX_SOCKET:+-S "$TMUX_SOCKET"} "$@"
#   }
# fi
#
# _tmux_version=$(tmux -V | awk '{gsub(/[^0-9.]/, "", $2); print ($2+0) * 100}')
#
# _is_true() {
#   [ "$1" = "true" ] || [ "$1" = "yes" ] || [ "$1" = "1" ]
# }
#
# _is_enabled() {
#   [ "$1" = "enabled" ]
# }
#
# _is_disabled() {
#   [ "$1" = "disabled" ]
# }
#
# _circled() {
#   circled_digits='⓪ ① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ⑱ ⑲ ⑳'
#   if [ "$1" -le 20 ] 2>/dev/null; then
#     i=$(( $1 + 1 ))
#     eval set -- "$circled_digits"
#     eval echo "\${$i}"
#   else
#     echo "$1"
#   fi
# }
#
# _decode_unicode_escapes() {
#   printf '%s' "$*" | perl -CS -pe 's/(\\u([0-9A-Fa-f]{1,4})|\\U([0-9A-Fa-f]{1,8}))/chr(hex($2.$3))/eg' 2>/dev/null
# }
#
# if command -v pkill > /dev/null 2>&1; then
#   _pkillf() {
#     pkill -f "$@" || true
#   }
# else
#   case "$_uname_s" in
#     *CYGWIN*)
#       _pkillf() {
#         while IFS= read -r pid; do
#           kill "$pid" || true
#         done  << EOF
# $(grep -Eao "$@" /proc/*/cmdline | xargs -0 | sed -E -n 's,/proc/([0-9]+)/.+$,\1,pg')
# EOF
#       }
#       ;;
#     *)
#       # shellcheck disable=SC2009
#       _pkillf() {
#         while IFS= read -r pid; do
#           kill "$pid" || true
#         done  << EOF
# $(ps -x -o pid= -o command= | grep -E "$@" | cut -d' ' -f1)
# EOF
#       }
#       ;;
#   esac
# fi
#
# _bar() {
#   bar_palette=$(printf '%s' "$1" | tr ';' ',')
#   bar_symbol_empty=$2
#   bar_symbol_full=$3
#   bar_length=$4
#   bar_value=$5
#
#   if [ "$bar_length" = "auto" ]; then
#     columns=${6:-$(tmux -q display -p '#{client_width}' 2> /dev/null || echo 80)}
#     if [ "$columns" -ge 160 ]; then
#       bar_length=12
#     elif [ "$columns" -ge 130 ]; then
#       bar_length=10
#     elif [ "$columns" -ge 120 ]; then
#       bar_length=8
#     elif [ "$columns" -ge 100 ]; then
#       bar_length=6
#     else
#       bar_length=4
#     fi
#   fi
#
#   if echo "$bar_palette" | grep -q -E '^heat|gradient(,[#a-z0-9]{7,9})?$'; then
#     # shellcheck disable=SC2086
#     { set -f; IFS=,; set -- $bar_palette; unset IFS; set +f; }
#     palette_style=$1
#     bg=${2:-none}
#     [ "$palette_style" = "gradient" ] && \
#       palette="196 202 208 214 220 226 190 154 118 82 46"
#     [ "$palette_style" = "heat" ] && \
#       palette="243 245 247 144 143 142 184 214 208 202 196"
#
#     palette=$(echo "$palette" | awk -v n="$bar_length" '{ for (i = 0; i < n; ++i) printf $(1 + (i * NF / n))" " }')
#     eval set -- "$palette"
#
#     full=$(awk "BEGIN { printf \"%.0f\", ($bar_value) * $bar_length }")
#     bar="#[bg=$bg]"
#     # shellcheck disable=SC2046
#     [ "$full" -gt 0 ] && \
#       bar="$bar$(printf "#[fg=colour%s]$bar_symbol_full" $(echo "$palette" | cut -d' ' -f1-"$full"))"
#     # shellcheck disable=SC2046
#     empty=$((bar_length - full))
#     # shellcheck disable=SC2046
#     [ "$empty" -gt 0 ] && \
#       bar="$bar$(printf "#[fg=colour%s]$bar_symbol_empty" $(echo "$palette" | cut -d' ' -f$((full + 1))-$((full + empty))))"
#       eval bar="$bar#[fg=colour\${$((full == 0 ? 1 : full))}]"
#   elif echo "$bar_palette" | grep -q -E '^(([#a-z0-9]{7,9}|none),?){3}$'; then
#     # shellcheck disable=SC2086
#     { set -f; IFS=,; set -- $bar_palette; unset IFS; set +f; }
#     full_fg=$1
#     empty_fg=$2
#     bg=$3
#
#     full=$(awk "BEGIN { printf \"%.0f\", ($bar_value) * $bar_length }")
#     [ "$bg" != "none" ] && \
#       bar="#[bg=$bg]"
#     #shellcheck disable=SC2046
#     [ "$full" -gt 0 ] && \
#       bar="$bar#[fg=$full_fg]$(printf "%0.s$bar_symbol_full" $(seq 1 "$full"))"
#     empty=$((bar_length - full))
#     #shellcheck disable=SC2046
#     [ "$empty" -gt 0 ] && \
#       bar="$bar#[fg=$empty_fg]$(printf "%0.s$bar_symbol_empty" $(seq 1 "$empty"))" && \
#       bar="$bar#[fg=$empty_fg]"
#   fi
#
#   printf '%s' "$bar"
# }
#
# _hbar() {
#   hbar_palette=$(printf '%s' "$1" | tr ';' ',')
#   hbar_value=$2
#
#   if echo "$hbar_palette" | grep -q -E '^heat|gradient(,[#a-z0-9]{7,9})?$'; then
#     # shellcheck disable=SC2086
#     { set -f; IFS=,; set -- $hbar_palette; unset IFS; set +f; }
#     palette_style=$1
#     [ "$palette_style" = "gradient" ] && \
#       palette="196 202 208 214 220 226 190 154 118 82 46"
#     [ "$palette_style" = "heat" ] && \
#       palette="233 234 235 237 239 241 243 245 247 144 143 142 184 214 208 202 196"
#
#     palette=$(echo "$palette" | awk -v n=8 '{ for (i = 0; i < n; ++i) printf $(1 + (i * NF / n))" " }')
#     eval set -- "$palette"
#
#     full=$(awk "BEGIN { printf \"%.0f\", ($hbar_value) * 8 }")
#     eval hbar_fg="colour\${$((full == 0 ? 1 : full))}"
#   elif echo "$hbar_palette" | grep -q -E '^([#a-z0-9]{7,9},?){3}$'; then
#     # shellcheck disable=SC2086
#     { set -f; IFS=,; set -- $hbar_palette; unset IFS; set +f; }
#
#     # shellcheck disable=SC2046
#     eval $(awk "BEGIN { printf \"hbar_fg=$%d\", (($hbar_value) - 0.001) * $# + 1 }")
#   fi
#
#   eval set -- "▏ ▎ ▍ ▌ ▋ ▊ ▉ █"
#   # shellcheck disable=SC2046
#   eval $(awk "BEGIN { printf \"hbar_symbol=$%d\", ($hbar_value) * ($# - 1) + 1 }")
#   hbar="#[bg=none]#[fg=${hbar_fg?}]${hbar_symbol?}"
#
#   printf '%s' "$hbar"
# }
#
# _vbar() {
#   vbar_palette=$(printf '%s' "$1" | tr ';' ',')
#   vbar_value=$2
#
#   if echo "$vbar_palette" | grep -q -E '^heat|gradient(,[#a-z0-9]{7,9})?$'; then
#     # shellcheck disable=SC2086
#     { set -f; IFS=,; set -- $vbar_palette; unset IFS; set +f; }
#     palette_style=$1
#     [ "$palette_style" = "gradient" ] && \
#       palette="196 202 208 214 220 226 190 154 118 82 46"
#     [ "$palette_style" = "heat" ] && \
#       palette="233 234 235 237 239 241 243 245 247 144 143 142 184 214 208 202 196"
#
#     palette=$(echo "$palette" | awk -v n=8 '{ for (i = 0; i < n; ++i) printf $(1 + (i * NF / n))" " }')
#     eval set -- "$palette"
#
#     full=$(awk "BEGIN { printf \"%.0f\", ($vbar_value) * 8 }")
#     eval vbar_fg="colour\${$((full == 0 ? 1 : full))}"
#   elif echo "$vbar_palette" | grep -q -E '^([#a-z0-9]{7,9},?){3}$'; then
#     # shellcheck disable=SC2086
#     { set -f; IFS=,; set -- $vbar_palette; unset IFS; set +f; }
#
#     # shellcheck disable=SC2046
#     eval $(awk "BEGIN { printf \"vbar_fg=$%d\", (($vbar_value) - 0.001) * $# + 1 }")
#   fi
#
#   eval set -- "▁ ▂ ▃ ▄ ▅ ▆ ▇ █"
#   # shellcheck disable=SC2046
#   eval $(awk "BEGIN { printf \"vbar_symbol=$%d\", ($vbar_value) * ($# - 1) + 1 }")
#   vbar="#[bg=none]#[fg=${vbar_fg?}]${vbar_symbol?}"
#
#   printf '%s' "$vbar"
# }
#
# _maximize_pane() {
#   current_session=${1:-$(tmux display -p '#{session_name}')}
#   current_pane=${2:-$(tmux display -p '#{pane_id}')}
#
#   dead_panes=$(tmux list-panes -s -t "$current_session" -F '#{pane_dead} #{pane_id} #{pane_start_command}' | grep -E -o '^1 %.+maximized.+$' || true)
#   restore=$(printf "%s" "$dead_panes" | sed -n -E -e "s/^1 $current_pane .+maximized.+'(%[0-9]+)'\"?$/tmux swap-pane -s \1 -t $current_pane \; kill-pane -t $current_pane/p"\
#                                            -e "s/^1 (%[0-9]+) .+maximized.+'$current_pane'\"?$/tmux swap-pane -s \1 -t $current_pane \; kill-pane -t \1/p")
#
#   if [ -z "$restore" ]; then
#     [ "$(tmux list-panes -t "$current_session:" | wc -l | sed 's/^ *//g')" -eq 1 ] && tmux display "Can't maximize with only one pane" && return
#     info=$(tmux new-window -t "$current_session:" -F "#{session_name}:#{window_index}.#{pane_id}" -P "maximized... 2>/dev/null & \"$TMUX_PROGRAM\" ${TMUX_SOCKET:+-S \"$TMUX_SOCKET\"} setw -t \"$current_session:\" remain-on-exit on; printf \"\\033[\$(tput lines);0fPane has been maximized, press <prefix>+ to restore\n\" '$current_pane'")
#     session_window=${info%.*}
#     new_pane=${info#*.}
#
#     retry=20
#     while [ "$("$TMUX_PROGRAM" ${TMUX_SOCKET:+-S "$TMUX_SOCKET"} list-panes -t "$session_window" -F '#{session_name}:#{window_index}.#{pane_id} #{pane_dead}' 2>/dev/null)" != "$info 1" ] && [ "$retry" -ne 0 ]; do
#       sleep 0.1
#       retry=$((retry - 1))
#     done
#     if [ "$retry" -eq 0 ]; then
#       tmux display 'Unable to maximize pane'
#     fi
#
#     tmux setw -t "$session_window" remain-on-exit off \; swap-pane -s "$current_pane" -t "$new_pane"
#   else
#     $restore || tmux kill-pane
#   fi
# }
#
# _toggle_mouse() {
#   old=$(tmux show -gv mouse)
#   new=""
#
#   if [ "$old" = "on" ]; then
#     new="off"
#   else
#     new="on"
#   fi
#
#   tmux set -g mouse $new
# }
#
# _battery_info() {
#   battery_count=0
#   battery_charge=0
#   case "$_uname_s" in
#     *Darwin*)
#       while IFS= read -r line; do
#         [ -z "$line" ] && continue
#         percentage=$(printf '%s' "$line" | grep -E -o '[0-9]+%' || echo "0%")
#         battery_charge=$(awk -v charge="$battery_charge" -v percentage="${percentage%%%}" 'BEGIN { print charge + percentage / 100 }')
#         battery_count=$((battery_count + 1))
#       done  << EOF
# $(pmset -g batt | grep 'InternalBattery')
# EOF
#       ;;
#     *Linux*)
#       while IFS= read -r batpath; do
#         [ -z "$batpath" ] && continue
#         grep -i -q device "$batpath/scope" 2> /dev/null && continue
#
#         bat_capacity="$batpath/capacity"
#         if [ -r "$bat_capacity" ]; then
#           battery_charge=$(awk -v charge="$battery_charge" -v capacity="$(cat "$bat_capacity")" 'BEGIN { print charge + (capacity > 100 ? 100 : capacity) / 100 }')
#         else
#           bat_energy_full="$batpath/energy_full"
#           bat_energy_now="$batpath/energy_now"
#           if [ -r "$bat_energy_full" ] && [ -r "$bat_energy_now" ]; then
#             battery_charge=$(awk -v charge="$battery_charge" -v energy_now="$(cat "$bat_energy_now")" -v energy_full="$(cat "$bat_energy_full")" 'BEGIN { print charge + energy_now / energy_full }')
#           fi
#         fi
#         battery_count=$((battery_count + 1))
#       done  << EOF
# $(find /sys/class/power_supply -maxdepth 1 -iname '*bat*')
# EOF
#       ;;
#     *CYGWIN*|*MSYS*|*MINGW*)
#       while IFS= read -r line; do
#         [ -z "$line" ] && continue
#         battery_charge=$(printf '%s' "$line" | awk -v charge="$battery_charge" '{ print charge + $2 / 100 }')
#         battery_count=$((battery_count + 1))
#       done  << EOF
# $(wmic path Win32_Battery get BatteryStatus, EstimatedChargeRemaining 2> /dev/null | tr -d '\r' | tail -n +2 || true)
# EOF
#       ;;
#     *OpenBSD*)
#       for batid in 0 1 2; do
#         sysctl -n "hw.sensors.acpibat$batid.raw0" 2>&1 | grep -q 'not found' && continue
#         if sysctl -n "hw.sensors.acpibat$batid" | grep -q amphour; then
#           battery_charge=$(awk -v charge="$battery_charge" -v remaining="$(sysctl -n hw.sensors.acpibat$batid.amphour3 | cut -d' ' -f1)" -v full="$(sysctl -n hw.sensors.acpibat$batid.amphour0 | cut -d' ' -f1)" 'BEGIN { print charge + remaining / full }')
#         else
#           battery_charge=$(awk -v charge="$battery_charge" -v remaining="$(sysctl -n hw.sensors.acpibat$batid.watthour3 | cut -d' ' -f1)" -v full="$(sysctl -n hw.sensors.acpibat$batid.watthour0 | cut -d' ' -f1)" 'BEGIN { print charge + remaining / full }')
#         fi
#         battery_count=$((battery_count + 1))
#       done
#       ;;
#     *FreeBSD*)
#       battery_charge=$(awk -v charge="$(sysctl -n 'hw.acpi.battery.life')" 'BEGIN { print charge / 100 }')
#       battery_count=1
#       ;;
#   esac
#   if [ "$battery_count" -ne 0 ]; then
#     battery_charge=$(awk -v charge="$battery_charge" -v count="$battery_count" 'BEGIN { print charge / count }')
#   fi
#
#   if [ "$battery_charge" = 0 ]; then
#     tmux  set -ug '@battery_percentage' \;\
#           set -ug '@battery_charge'
#   else
#     battery_percentage="$(awk "BEGIN { printf \"%.0f%%\", ($battery_charge) * 100 }")"
#
#     tmux  set -g '@battery_percentage' "$battery_percentage" \;\
#           set -g '@battery_charge' "$battery_charge"
#   fi
# }
#
# _battery_status() {
#   battery_status_charging=$1
#   battery_status_discharging=$2
#
#   case "$_uname_s" in
#     *Darwin*)
#       while IFS= read -r line; do
#         [ -z "$line" ] && continue
#         battery_discharging=$(printf '%s' "$line" | grep -qi "discharging" && echo "true" || echo "false")
#       done  << EOF
# $(pmset -g batt | grep 'InternalBattery')
# EOF
#       ;;
#     *Linux*)
#       while IFS= read -r batpath; do
#         [ -z "$batpath" ] && continue
#         grep -i -q device "$batpath/scope" 2> /dev/null && continue
#
#         battery_discharging=$(grep -qi "discharging" "$batpath/status" && echo "true" || echo "false")
#       done  << EOF
# $(find /sys/class/power_supply -maxdepth 1 -iname '*bat*')
# EOF
#       ;;
#     *CYGWIN*|*MSYS*|*MINGW*)
#       while IFS= read -r line; do
#         [ -z "$line" ] && continue
#         battery_discharging=$(printf '%s' "$line" | awk '{ s = ($1 == 1) ? "true" : "false"; print s }')
#       done  << EOF
# $(wmic path Win32_Battery get BatteryStatus, EstimatedChargeRemaining 2> /dev/null | tr -d '\r' | tail -n +2 || true)
# EOF
#       ;;
#     *OpenBSD*)
#       for batid in 0 1 2; do
#         battery_discharging=$(sysctl -n "hw.sensors.acpibat$batid.raw0" | grep -q 1 && echo "true" || echo "false")
#       done
#       ;;
#     *FreeBSD*)
#       battery_discharging=$(sysctl -n 'hw.acpi.battery.state' | grep -q 1 && echo "true" || echo "false")
#       ;;
#   esac
#
#   if [ -z "$battery_discharging" ]; then
#     tmux set -ug '@battery_status'
#     return
#   fi
#
#   if [ "$battery_discharging" = "true" ]; then
#     battery_status="$battery_status_discharging"
#   else
#     battery_status="$battery_status_charging"
#   fi
#
#   tmux set -g '@battery_status' "$battery_status"
# }
#
# _pane_info() {
#   pane_pid="$1"
#   pane_tty="${2##/dev/}"
#   case "$_uname_s" in
#     *CYGWIN*)
#       ps -al | tail -n +2 | awk -v pane_pid="$pane_pid" -v tty="$pane_tty" '
#         ((/ssh/ && !/-W/ && !/tsh proxy ssh/ &!/sss_ssh_knownhostsproxy/) || !/ssh/) && !/tee/ && $5 == tty {
#           user[$1] = $6; if (!child[$2]) child[$2] = $1
#         }
#         END {
#           pid = pane_pid
#           while (child[pid])
#             pid = child[pid]
#
#           file = "/proc/" pid "/cmdline"; getline command < file; close(file)
#           gsub(/\0/, " ", command)
#           "id -un " user[pid] | getline username
#           print pid":"username":"command
#         }
#       '
#       ;;
#     *Linux*)
#       ps -t "$pane_tty" --sort=lstart -o user=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -o pid= -o ppid= -o command= | awk -v pane_pid="$pane_pid" '
#         ((/ssh/ && !/-W/ && !/tsh proxy ssh/ && !/sss_ssh_knownhostsproxy/) || !/ssh/) && !/tee/ {
#           user[$2] = $1; if (!child[$3]) child[$3] = $2; pid=$2; $1 = $2 = $3 = ""; command[pid] = substr($0,4)
#         }
#         END {
#           pid = pane_pid
#           while (child[pid])
#             pid = child[pid]
#
#           print pid":"user[pid]":"command[pid]
#         }
#       '
#       ;;
#     *)
#       ps -t "/dev/$pane_tty" -o user=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -o pid= -o ppid= -o command= | awk -v pane_pid="$pane_pid" '
#         ((/ssh/ && !/-W/ && !/tsh proxy ssh/ && !/sss_ssh_knownhostsproxy/) || !/ssh/) && !/tee/ {
#           user[$2] = $1; if (!child[$3]) child[$3] = $2; pid=$2; $1 = $2 = $3 = ""; command[pid] = substr($0,4)
#         }
#         END {
#           pid = pane_pid
#           while (child[pid])
#             pid = child[pid]
#
#           print pid":"user[pid]":"command[pid]
#         }
#       '
#       ;;
#   esac
# }
#
# _ssh_or_mosh_args() {
#   case "$1" in
#     *ssh*)
#       args=$(printf '%s' "$1" | perl -n -e 'print if s/.*?\bssh[\w_-]*\s*(.*)/\1/')
#       ;;
#     *mosh-client*)
#       args=$(printf '%s' "$1" | sed -E -e 's/.*mosh-client -# (.*)\|.*$/\1/' -e 's/-[^ ]*//g' -e 's/\d:\d//g')
#       ;;
#   esac
#
#  printf '%s' "$args"
# }
#
# _username() {
#   pane_pid=${1:-$(tmux display -p '#{pane_pid}')}
#   pane_tty=${2:-$(tmux display -p '#{b:pane_tty}')}
#   ssh_only=$3
#
#   pane_info=$(_pane_info "$pane_pid" "$pane_tty")
#   command=${pane_info#*:}
#   command=${command#*:}
#
#   ssh_or_mosh_args=$(_ssh_or_mosh_args "$command")
#   if [ -n "$ssh_or_mosh_args" ]; then
#     # shellcheck disable=SC2086
#     username=$(ssh -G $ssh_or_mosh_args 2>/dev/null | awk '/^user / { print $2; exit }')
#     # shellcheck disable=SC2086
#     [ -z "$username" ] && username=$(ssh $ssh_or_mosh_args -T -o ControlPath=none -o ProxyCommand="sh -c 'echo %%username%% %r >&2'" 2>&1 | awk '/^%username% / { print $2; exit }')
#     # shellcheck disable=SC2086
#     [ -z "$username" ] && username=$(ssh $ssh_or_mosh_args -v -T -o ControlPath=none -o ProxyCommand=false -o IdentityFile='%%username%%/%r' 2>&1 | awk '/%username%/ { print substr($4,12); exit }')
#   else
#     if ! _is_true "$ssh_only"; then
#       username=${pane_info#*:}
#       username=${username%%:*}
#     fi
#   fi
#
#   printf '%s\n' "$username"
# }
#
# _hostname() {
#   pane_pid=${1:-$(tmux display -p '#{pane_pid}')}
#   pane_tty=${2:-$(tmux display -p '#{b:pane_tty}')}
#   ssh_only=$3
#   full=$4
#   h_or_H=$5
#
#   pane_info=$(_pane_info "$pane_pid" "$pane_tty")
#   command=${pane_info#*:}
#   command=${command#*:}
#
#   ssh_or_mosh_args=$(_ssh_or_mosh_args "$command")
#   if [ -n "$ssh_or_mosh_args" ]; then
#     # shellcheck disable=SC2086
#     hostname=$(ssh -G $ssh_or_mosh_args 2>/dev/null | awk '/^hostname / { print $2; exit }')
#     # shellcheck disable=SC2086
#     [ -z "$hostname" ] && hostname=$(ssh -T -o ControlPath=none -o ProxyCommand="sh -c 'echo %%hostname%% %h >&2'" $ssh_or_mosh_args 2>&1 | awk '/^%hostname% / { print $2; exit }')
#
#     if ! _is_true "$full"; then
#       case "$hostname" in
#           *[a-z-].*)
#               hostname=${hostname%%.*}
#               ;;
#           127.0.0.1)
#               hostname="localhost"
#               ;;
#       esac
#     fi
#   else
#     if ! _is_true "$ssh_only"; then
#       hostname="$h_or_H"
#     fi
#   fi
#
#   printf '%s\n' "$hostname"
# }
#
# _root() {
#   pane_pid=${1:-$(tmux display -p '#{pane_pid}')}
#   pane_tty=${2:-$(tmux display -p '#{b:pane_tty}')}
#   root=$3
#
#   username=$(_username "$pane_pid" "$pane_tty" false)
#
#   [ "$username" = "root" ] && echo "$root"
# }
#
# _uptime() {
#   case "$_uname_s" in
#     *Darwin*|*FreeBSD*)
#       boot=$(sysctl -n kern.boottime 2>/dev/null | awk -F'[ ,:]+' '{ print $4 }')
#       now=$(date +%s)
#       ;;
#     *Linux*|*CYGWIN*|*MSYS*|*MINGW*)
#       boot=0
#       now=$(cut -d' ' -f1 < /proc/uptime)
#       ;;
#     *OpenBSD*)
#       boot=$(sysctl -n kern.boottime)
#       now=$(date +%s)
#   esac
#   # shellcheck disable=SC1004
#   awk -v tmux="$TMUX_PROGRAM ${TMUX_SOCKET:+-S "$TMUX_SOCKET"}" -v boot="$boot" -v now="$now" '
#     BEGIN {
#       uptime = now - boot
#       y = int(uptime / 31536000)
#       dy = int(uptime / 86400) % 365
#       d = int(uptime / 86400)
#       h = int(uptime / 3600) % 24
#       m = int(uptime / 60) % 60
#       s = int(uptime) % 60
#
#       system(tmux " set -g @uptime_y " y + 0    " \\;" \
#                   " set -g @uptime_dy " dy + 0  " \\;" \
#                   " set -g @uptime_d " d + 0    " \\;" \
#                   " set -g @uptime_h " h + 0    " \\;" \
#                   " set -g @uptime_m " m + 0    " \\;" \
#                   " set -g @uptime_s " s + 0)
#     }'
# }
#
# _loadavg() {
#   case "$_uname_s" in
#     *Darwin*|*FreeBSD*)
#       tmux set -g @loadavg "$(sysctl -n vm.loadavg 2>/dev/null | cut -d' ' -f2)"
#       ;;
#     *Linux*|*CYGWIN*)
#       tmux set -g @loadavg "$(cut -d' ' -f1 < /proc/loadavg)"
#       ;;
#     *OpenBSD*)
#       tmux set -g @loadavg "$(sysctl -n vm.loadavg 2>/dev/null | cut -d' ' -f1)"
#       ;;
#   esac
# }
#
# _new_window_ssh() {
#   pane_pid=${1:-$(tmux display -p '#{pane_pid}')}
#   pane_tty=${2:-$(tmux display -p '#{b:pane_tty}')}
#   shift 2
#
#   pane_info=$(_pane_info "$pane_pid" "$pane_tty")
#   command=${pane_info#*:}
#   command=${command#*:}
#
#   case "$command" in
#     *mosh-client*)
#       # shellcheck disable=SC2046
#        tmux new-window "$@" mosh $(echo "$command" | sed -E -e 's/.*mosh-client -# (.*)\|.*$/\1/')
#      ;;
#     *ssh*)
#       # shellcheck disable=SC2046
#       tmux new-window "$@" $(echo "$command" | sed -e 's/;/\\;/g')
#       ;;
#     *)
#       tmux new-window "$@"
#   esac
# }
#
# _new_window() {
#   _new_window_ssh "$@"
# }
#
# _split_window_ssh() {
#   pane_pid=${1:-$(tmux display -p '#{pane_pid}')}
#   pane_tty=${2:-$(tmux display -p '#{b:pane_tty}')}
#   shift 2
#
#   pane_info=$(_pane_info "$pane_pid" "$pane_tty")
#   command=${pane_info#*:}
#   command=${command#*:}
#
#   case "$command" in
#     *mosh-client*)
#       # shellcheck disable=SC2046
#        tmux split-window "$@" mosh $(echo "$command" | sed -E -e 's/.*mosh-client -# (.*)\|.*$/\1/')
#      ;;
#     *ssh*)
#       # shellcheck disable=SC2046
#       tmux split-window "$@" $(echo "$command" | sed -e 's/;/\\;/g')
#       ;;
#     *)
#       tmux split-window "$@"
#   esac
# }
#
# _split_window() {
#   _split_window_ssh "$@"
# }
#
# _apply_tmux_256color() {
#   case "$(tmux show -gv default-terminal)" in
#     tmux-256color|tmux-direct)
#       return
#       ;;
#   esac
#
#   # when tmux-256color is available, use it
#   # on macOS though, make sure to use /usr/bin/infocmp to probe if it's availalbe system wide
#   case "$_uname_s" in
#     *Darwin*)
#       if /usr/bin/infocmp -x tmux-256color > /dev/null 2>&1; then
#         tmux set -g default-terminal 'tmux-256color'
#       fi
#       ;;
#      *)
#       if command infocmp -x tmux-256color > /dev/null 2>&1; then
#         tmux set -g default-terminal 'tmux-256color'
#       fi
#       ;;
#   esac
# }
#
# _apply_24b() {
#   tmux_conf_theme_24b_colour=${tmux_conf_theme_24b_colour:-auto}
#   tmux_conf_24b_colour=${tmux_conf_24b_colour:-$tmux_conf_theme_24b_colour}
#   if [ "$tmux_conf_24b_colour" = "auto" ]; then
#     case "$COLORTERM" in
#       truecolor|24bit)
#         apply_24b=true
#         ;;
#     esac
#     if [ "$apply_24b" = "" ] && [ "$(tput colors)" = "16777216" ]; then
#       apply_24b=true
#     fi
#   elif _is_true "$tmux_conf_24b_colour"; then
#     apply_24b=true
#   fi
#   if [ "$apply_24b" = "true" ]; then
#     case "$TERM" in
#       screen-*|tmux-*)
#         ;;
#       *)
#         tmux set-option -ga terminal-overrides ",*256col*:Tc"
#         ;;
#     esac
#   fi
# }
#
# _apply_bindings() {
#   cfg=$(mktemp) && trap 'rm -f $cfg*' EXIT
#
#   tmux_conf_preserve_stock_bindings=${tmux_conf_preserve_stock_bindings:-false}
#   tmux list-keys | grep -vF 'TMUX_CONF_LOCAL' | grep -E 'new-window|split(-|_)window|new-session|copy-selection|copy-pipe' > "$cfg"
#   if _is_true "$tmux_conf_preserve_stock_bindings"; then
#     probe_socket="$(dirname "$TMUX_SOCKET")/tmux-stock-bindings-$$"
#     TMUX_SOCKET="$probe_socket" tmux -f /dev/null list-keys >> "$cfg"
#     rm -f "%probe_socket"
#   fi
#
#   # tmux 3.0 doesn't include 02254d1e5c881be95fd2fc37b4c4209640b6b266 and the
#   # output of list-keys can be truncated
#   perl -p -i -e "s/'#\{\?window_zoomed_flag,Unzoom,Zoom\}' 'z' \{resize-pane -$/'#{?window_zoomed_flag,Unzoom,Zoom}' 'z' {resize-pane -Z}\"/g" "$cfg"
#
#   tmux_conf_new_window_retain_current_path=${tmux_conf_new_window_retain_current_path:-true}
#   if ! _is_disabled "$tmux_conf_new_window_retain_current_path"; then
#     perl -p -i -e "
#       s/\brun-shell\b\s+(\"|')cut\s+-c3-\s+(.+?)\s+\|\s+sh\s+-s\s+_new_window\s+#\{pane_pid\}\s+#\{b:pane_tty\}([^\n\1]*?)(?:\s+-c\s+((?:\\\\{1,3}\")?|\"?|'?)#\{pane_current_path\}\4)([^\n\1]*?)\1/run-shell \1cut -c3- \2 | sh -s _new_window #\{pane_pid\} #\{b:pane_tty\}\3\5\1/g
#       ;
#       s/\brun-shell\b\s+(\"|')cut\s+-c3-\s+.+?\s+\|\s+sh\s+-s\s+_new_window\s+#\{pane_pid\}\s+#\{b:pane_tty\}(\s+.+?)?\1/new-window\2/g
#       ;
#       s/\bnew-window\b([^;}\n]*?)(?:\s+-c\s+((?:\\\\\")?|\"?|'?)#\{pane_current_path\}\2)/new-window\1/g" \
#       "$cfg"
#   fi
#
#   perl -p -i -e "
#     s,\bnew-window\b((?:(?:[ \t]+-[bdfhIvP])|(?:[ \t]+-[celtF][ \t]+(?!\bssh\b)[^\s]+))*)?(?:\s+(\bssh\b))((?:(?:[ \t]+-[bdfhIvP])|(?:[ \t]+-[celtF][ \t]+(?!\bssh\b)[^\s]+))*)?,run-shell 'cut -c3- \"$TMUX_CONF\" | sh -s _new_window_ssh #\{pane_pid\} #\{b:pane_tty\}\1',g if /\bnew-window\b((?:(?:[ \t]+-[bdfhIvP])|(?:[ \t]+-[celtF][ \t]+(?!ssh)[^\s]+))*)?(?:\s+(ssh))((?:(?:[ \t]+-[bdfhIvP])|(?:[ \t]+-[celtF][ \t]+(?!ssh)[^\s]+))*)?/"\
#   "$cfg"
#
#   tmux_conf_new_window_reconnect_ssh=${tmux_conf_new_window_reconnect_ssh:-false}
#   if ! _is_disabled "$tmux_conf_new_window_reconnect_ssh" && _is_true "$tmux_conf_new_window_reconnect_ssh"; then
#     perl -p -i -e "s,\bnew-window\b([^;}\n\"]*),run-shell 'cut -c3- \"$TMUX_CONF\" | sh -s _new_window #\{pane_pid\} #\{b:pane_tty\}\1',g" "$cfg"
#   fi
#
#   tmux_conf_new_window_retain_current_path=${tmux_conf_new_window_retain_current_path:-false}
#   if ! _is_disabled "$tmux_conf_new_window_retain_current_path" && _is_true "$tmux_conf_new_window_retain_current_path"; then
#     perl -p -i -e "
#       s/\bnew-window\b(?!\s+(?:-|}))/{$&}/g if /\bdisplay-menu\b/
#       ;
#       s/\bnew-window\b/new-window -c '#{pane_current_path}'/g
#       ;
#       s/\brun-shell\b\s+'cut\s+-c3-\s+(.+?)\s+\|\s+sh\s+-s\s+_new_window(_ssh)?\s+#\{pane_pid\}\s+#\{b:pane_tty\}([^}\n']*)'/run-shell 'cut -c3- \1 | sh -s _new_window\2 #\{pane_pid\} #\{b:pane_tty\} -c \\\\\"#\{pane_current_path\}\\\\\"\3'/g if /\bdisplay-menu\b/
#       ;
#       s/\brun-shell\b\s+'cut\s+-c3-\s+(.+?)\s+\|\s+sh\s+-s\s+_new_window(_ssh)?\s+#\{pane_pid\}\s+#\{b:pane_tty\}([^}\n']*)'/run-shell 'cut -c3- \1 | sh -s _new_window\2 #\{pane_pid\} #\{b:pane_tty\} -c \"#\{pane_current_path\}\"\3'/g" \
#       "$cfg"
#   fi
#
#   tmux_conf_new_pane_retain_current_path=${tmux_conf_new_pane_retain_current_path:-true}
#   if ! _is_disabled "$tmux_conf_new_pane_retain_current_path"; then
#     perl -p -i -e "
#       s/\brun-shell\b\s+(\"|')cut\s+-c3-\s+(.+?)\s+\|\s+sh\s+-s\s+_split_window\s+#\{pane_pid\}\s+#\{b:pane_tty\}([^\n\1]*?)(?:\s+-c\s+((?:\\\\{1,3}\")?|\"?|'?)#\{pane_current_path\}\4)([^\n\1]*?)\1/run-shell \1cut -c3- \2 | sh -s _split_window #\{pane_pid\} #\{b:pane_tty\}\3\5\1/g
#       ;
#       s/\brun-shell\b\s+(\"|')cut\s+-c3-\s+.+?\s+\|\s+sh\s+-s\s+_split_window\s+#\{pane_pid\}\s+#\{b:pane_tty\}(\s+.+?)?\1/split-window\2/g
#       ;
#       s/\bsplit-window\b([^;}\n]*?)(?:\s+-c\s+((?:\\\\\")?|\"?|'?)#\{pane_current_path\}\2)/split-window\1/g" \
#       "$cfg"
#   fi
#
#   perl -p -i -e "
#     s,\bsplit-window\b((?:(?:[ \t]+-[bdfhIvP])|(?:[ \t]+-[celtF][ \t]+(?!\bssh\b)[^\s]+))*)?(?:\s+(\bssh\b))((?:(?:[ \t]+-[bdfhIvP])|(?:[ \t]+-[celtF][ \t]+(?!\bssh\b)[^\s]+))*)?,run-shell 'cut -c3- \"$TMUX_CONF\" | sh -s _split_window_ssh #\{pane_pid\} #\{b:pane_tty\}\1',g if /\bsplit-window\b((?:(?:[ \t]+-[bdfhIvP])|(?:[ \t]+-[celtF][ \t]+(?!ssh)[^\s]+))*)?(?:\s+(ssh))((?:(?:[ \t]+-[bdfhIvP])|(?:[ \t]+-[celtF][ \t]+(?!ssh)[^\s]+))*)?/"\
#   "$cfg"
#
#   tmux_conf_new_pane_reconnect_ssh=${tmux_conf_new_pane_reconnect_ssh:-false}
#   if ! _is_disabled "$tmux_conf_new_pane_reconnect_ssh" && _is_true "$tmux_conf_new_pane_reconnect_ssh"; then
#     perl -p -i -e "s,\bsplit-window\b([^;}\n\"]*),run-shell 'cut -c3- \"$TMUX_CONF\" | sh -s _split_window #\{pane_pid\} #\{b:pane_tty\}\1',g" "$cfg"
#   fi
#
#   if ! _is_disabled "$tmux_conf_new_pane_retain_current_path" && _is_true "$tmux_conf_new_pane_retain_current_path"; then
#     perl -p -i -e "
#       s/\bsplit-window\b(?!\s+(?:-|}))/{$&}/g if /\bdisplay-menu\b/
#       ;
#       s/\bsplit-window\b/split-window -c '#{pane_current_path}'\1/g
#       ;
#       s/\brun-shell\b\s+'cut\s+-c3-\s+(.+?)\s+\|\s+sh\s+-s\s+_split_window(_ssh)?\s+#\{pane_pid\}\s+#\{b:pane_tty\}([^}\n']*)'/run-shell 'cut -c3- \1 | sh -s _split_window\2 #\{pane_pid\} #\{b:pane_tty\} -c \\\\\"#\{pane_current_path\}\\\\\"\3'/g if /\bdisplay-menu\b/
#       ;
#       s/\brun-shell\b\s+'cut\s+-c3-\s+(.+?)\s+\|\s+sh\s+-s\s+_split_window(_ssh)?\s+#\{pane_pid\}\s+#\{b:pane_tty\}([^}\n']*)'/run-shell 'cut -c3- \1 | sh -s _split_window\2 #\{pane_pid\} #\{b:pane_tty\} -c \"#\{pane_current_path\}\"\3'/g" \
#       "$cfg"
#   fi
#
#   tmux_conf_new_session_prompt=${tmux_conf_new_session_prompt:-false}
#   if ! _is_disabled "$tmux_conf_new_session_prompt" && _is_true "$tmux_conf_new_session_prompt"; then
#     perl -p -i -e "
#       s/(?<!command-prompt -p )\b(new-session)\b(?!\s+(?:-|}))/{$&}/g if /\bdisplay-menu\b/
#       ;
#       s/(?<!\bcommand-prompt -p )\bnew-session\b(?! -s)/command-prompt -p new-session \"new-session -s '%%'\"/g" \
#       "$cfg"
#   else
#     perl -p -i -e "s/\bcommand-prompt\s+-p\s+new-session\s+\"new-session\s+-s\s+'%%'\"/new-session/g" "$cfg"
#   fi
#
#   tmux_conf_new_session_retain_current_path=${tmux_conf_new_session_retain_current_path:-false}
#   if ! _is_disabled "$tmux_conf_new_session_retain_current_path" && _is_true "$tmux_conf_new_session_retain_current_path"; then
#     perl -p -i -e "
#       s/(?<!\bcommand-prompt -p )\bnew-session\b/new-session -c '#{pane_current_path}'/g" \
#       "$cfg"
#   else
#     perl -p -i -e "
#       s/\bnew-session\b([^;}\n]*?)(?:\s+-c\s+((?:\\\\\")?|\"?|'?)#\{pane_current_path\}\2)/new-session\1/g" \
#       "$cfg"
#   fi
#
#   tmux_conf_copy_to_os_clipboard=${tmux_conf_copy_to_os_clipboard:-false}
#   command -v xsel > /dev/null 2>&1 && command='xsel -i -b'
#   ! command -v xsel > /dev/null 2>&1 && command -v xclip > /dev/null 2>&1 && command='xclip -i -selection clipboard > \/dev\/null 2>\&1'
#   [ "$XDG_SESSION_TYPE" = "wayland" ] && command -v wl-copy > /dev/null 2>&1 && command='wl-copy'
#   command -v pbcopy > /dev/null 2>&1 && command='pbcopy'
#   command -v clip.exe > /dev/null 2>&1 && command='clip\.exe'
#   [ -c /dev/clipboard ] && command='cat > \/dev\/clipboard'
#
#   if [ -n "$command" ]; then
#     if ! _is_disabled "$tmux_conf_copy_to_os_clipboard" && _is_true "$tmux_conf_copy_to_os_clipboard"; then
#       perl -p -i -e "s/(?!.*?$command)\bcopy-(?:selection|pipe)(-end-of-line|-and-cancel|-end-of-line-and-cancel|-no-clear)?\b/copy-pipe\1 '$command'/g" "$cfg"
#     else
#       if [ "$_tmux_version" -ge 320 ]; then
#         perl -p -i -e "s/\bcopy-pipe(-end-of-line|-and-cancel|end-of-line-and-cancel|-no-clear)?\b\s+(\"|')?$command\2?/copy-pipe\1/g" "$cfg"
#       else
#         perl -p -i -e "s/\bcopy-pipe(-end-of-line|-and-cancel|end-of-line-and-cancel|-no-clear)?\b\s+(\"|')?$command\2?/copy-selection\1/g" "$cfg"
#       fi
#     fi
#   fi
#
#   # until tmux >= 3.0, output of tmux list-keys can't be consumed back by tmux source-file without applying some escapings
#   awk < "$cfg" \
#     '{i = $2 == "-T" ? 4 : 5; gsub(/^[;]$/, "\\\\&", $i); gsub(/^[$"#~]$/, "'"'"'&'"'"'", $i); gsub(/^['"'"']$/, "\"&\"", $i); print}' > "$cfg.in"
#
#   # ignore bindings with errors
#   if ! tmux source-file "$cfg.in"; then
#     if tmux source-file -v /dev/null 2> /dev/null; then
#       verbose_flag='-v'
#     fi
#     while ! out=$(tmux source-file "${verbose_flag:+$verbose_flag}" "$cfg.in"); do
#       line=$(printf "%s" "$out" | tail -1 | cut -d':' -f2)
#       perl -n -i -e "if ($. != $line) { print }" "$cfg.in"
#     done
#   fi
#
#   tmux_conf_urlscan_options=${tmux_conf_urlscan_options:---compact --dedupe}
#   if command -v urlscan > /dev/null 2>&1; then
#     tmux bind U run "cut -c3- '#{TMUX_CONF}' | sh -s _urlscan '#{pane_id}' $tmux_conf_urlscan_options"
#   elif command -v urlview > /dev/null 2>&1; then
#     tmux bind U run "cut -c3- '#{TMUX_CONF}' | sh -s _urlview '#{pane_id}'"
#   fi
# }
#
# _apply_theme() {
#   tmux_conf_theme=${tmux_conf_theme:-enabled}
#   if ! _is_disabled "$tmux_conf_theme"; then
#
#     # -- default theme -------------------------------------------------------
#
#     tmux_conf_theme_colour_1=${tmux_conf_theme_colour_1:-#080808}     # dark gray
#     tmux_conf_theme_colour_2=${tmux_conf_theme_colour_2:-#303030}     # gray
#     tmux_conf_theme_colour_3=${tmux_conf_theme_colour_3:-#8a8a8a}     # light gray
#     tmux_conf_theme_colour_4=${tmux_conf_theme_colour_4:-#00afff}     # light blue
#     tmux_conf_theme_colour_5=${tmux_conf_theme_colour_5:-#ffff00}     # yellow
#     tmux_conf_theme_colour_6=${tmux_conf_theme_colour_6:-#080808}     # dark gray
#     tmux_conf_theme_colour_7=${tmux_conf_theme_colour_7:-#e4e4e4}     # white
#     tmux_conf_theme_colour_8=${tmux_conf_theme_colour_8:-#080808}     # dark gray
#     tmux_conf_theme_colour_9=${tmux_conf_theme_colour_9:-#ffff00}     # yellow
#     tmux_conf_theme_colour_10=${tmux_conf_theme_colour_10:-#ff00af}   # pink
#     tmux_conf_theme_colour_11=${tmux_conf_theme_colour_11:-#5fff00}   # green
#     tmux_conf_theme_colour_12=${tmux_conf_theme_colour_12:-#8a8a8a}   # light gray
#     tmux_conf_theme_colour_13=${tmux_conf_theme_colour_13:-#e4e4e4}   # white
#     tmux_conf_theme_colour_14=${tmux_conf_theme_colour_14:-#080808}   # dark gray
#     tmux_conf_theme_colour_15=${tmux_conf_theme_colour_15:-#080808}   # dark gray
#     tmux_conf_theme_colour_16=${tmux_conf_theme_colour_16:-#d70000}   # red
#     tmux_conf_theme_colour_17=${tmux_conf_theme_colour_17:-#e4e4e4}   # white
#
#     # -- panes ---------------------------------------------------------------
#
#     tmux_conf_theme_window_fg=${tmux_conf_theme_window_fg:-default}
#     tmux_conf_theme_window_bg=${tmux_conf_theme_window_bg:-default}
#     tmux_conf_theme_highlight_focused_pane=${tmux_conf_theme_highlight_focused_pane:-false}
#     tmux_conf_theme_focused_pane_fg=${tmux_conf_theme_focused_pane_fg:-default}
#     tmux_conf_theme_focused_pane_bg=${tmux_conf_theme_focused_pane_bg:-$tmux_conf_theme_colour_2}
#
#     window_style="fg=$tmux_conf_theme_window_fg,bg=$tmux_conf_theme_window_bg"
#     if _is_true "$tmux_conf_theme_highlight_focused_pane"; then
#       window_active_style="fg=$tmux_conf_theme_focused_pane_fg,bg=$tmux_conf_theme_focused_pane_bg"
#     else
#       window_active_style="default"
#     fi
#
#     tmux_conf_theme_pane_border_style=${tmux_conf_theme_pane_border_style:-thin}
#     tmux_conf_theme_pane_border=${tmux_conf_theme_pane_border:-$tmux_conf_theme_colour_2}
#     tmux_conf_theme_pane_active_border=${tmux_conf_theme_pane_active_border:-$tmux_conf_theme_colour_4}
#     tmux_conf_theme_pane_border_fg=${tmux_conf_theme_pane_border_fg:-$tmux_conf_theme_pane_border}
#     tmux_conf_theme_pane_active_border_fg=${tmux_conf_theme_pane_active_border_fg:-$tmux_conf_theme_pane_active_border}
#     case "$tmux_conf_theme_pane_border_style" in
#       fat)
#         tmux_conf_theme_pane_border_bg=${tmux_conf_theme_pane_border_bg:-$tmux_conf_theme_pane_border_fg}
#         tmux_conf_theme_pane_active_border_bg=${tmux_conf_theme_pane_active_border_bg:-$tmux_conf_theme_pane_active_border_fg}
#         ;;
#       thin|*)
#         tmux_conf_theme_pane_border_bg=${tmux_conf_theme_pane_border_bg:-default}
#         tmux_conf_theme_pane_active_border_bg=${tmux_conf_theme_pane_active_border_bg:-default}
#         ;;
#     esac
#
#     tmux_conf_theme_pane_indicator=${tmux_conf_theme_pane_indicator:-$tmux_conf_theme_colour_4}
#     tmux_conf_theme_pane_active_indicator=${tmux_conf_theme_pane_active_indicator:-$tmux_conf_theme_colour_4}
#
#     # -- status line ---------------------------------------------------------
#
#     tmux_conf_theme_left_separator_main=$(_decode_unicode_escapes "${tmux_conf_theme_left_separator_main-}")
#     tmux_conf_theme_left_separator_sub=$(_decode_unicode_escapes "${tmux_conf_theme_left_separator_sub-|}")
#     tmux_conf_theme_right_separator_main=$(_decode_unicode_escapes "${tmux_conf_theme_right_separator_main-}")
#     tmux_conf_theme_right_separator_sub=$(_decode_unicode_escapes "${tmux_conf_theme_right_separator_sub-|}")
#
#     tmux_conf_theme_message_fg=${tmux_conf_theme_message_fg:-$tmux_conf_theme_colour_1}
#     tmux_conf_theme_message_bg=${tmux_conf_theme_message_bg:-$tmux_conf_theme_colour_5}
#     tmux_conf_theme_message_attr=${tmux_conf_theme_message_attr:-bold}
#
#     tmux_conf_theme_message_command_fg=${tmux_conf_theme_message_command_fg:-$tmux_conf_theme_colour_5}
#     tmux_conf_theme_message_command_bg=${tmux_conf_theme_message_command_bg:-$tmux_conf_theme_colour_1}
#     tmux_conf_theme_message_command_attr=${tmux_conf_theme_message_command_attr:-bold}
#
#     tmux_conf_theme_mode_fg=${tmux_conf_theme_mode_fg:-$tmux_conf_theme_colour_1}
#     tmux_conf_theme_mode_bg=${tmux_conf_theme_mode_bg:-$tmux_conf_theme_colour_5}
#     tmux_conf_theme_mode_attr=${tmux_conf_theme_mode_attr:-bold}
#
#     tmux_conf_theme_status_fg=${tmux_conf_theme_status_fg:-$tmux_conf_theme_colour_3}
#     tmux_conf_theme_status_bg=${tmux_conf_theme_status_bg:-$tmux_conf_theme_colour_1}
#     tmux_conf_theme_status_attr=${tmux_conf_theme_status_attr:-none}
#
#     tmux_conf_theme_terminal_title=${tmux_conf_theme_terminal_title:-#h ❐ #S ● #I #W}
#
#     tmux_conf_theme_window_status_fg=${tmux_conf_theme_window_status_fg:-$tmux_conf_theme_colour_3}
#     tmux_conf_theme_window_status_bg=${tmux_conf_theme_window_status_bg:-$tmux_conf_theme_colour_1}
#     tmux_conf_theme_window_status_attr=${tmux_conf_theme_window_status_attr:-none}
#     tmux_conf_theme_window_status_format=${tmux_conf_theme_window_status_format:-'#I #W#{?#{||:#{window_bell_flag},#{window_zoomed_flag}}, ,}#{?window_bell_flag,!,}#{?window_zoomed_flag,Z,}'}
#
#     tmux_conf_theme_window_status_current_fg=${tmux_conf_theme_window_status_current_fg:-$tmux_conf_theme_colour_1}
#     tmux_conf_theme_window_status_current_bg=${tmux_conf_theme_window_status_current_bg:-$tmux_conf_theme_colour_4}
#     tmux_conf_theme_window_status_current_attr=${tmux_conf_theme_window_status_current_attr:-bold}
#     tmux_conf_theme_window_status_current_format=${tmux_conf_theme_window_status_current_format:-'#I #W#{?#{||:#{window_bell_flag},#{window_zoomed_flag}}, ,}#{?window_bell_flag,!,}#{?window_zoomed_flag,Z,}'}
#
#     tmux_conf_theme_window_status_activity_fg=${tmux_conf_theme_window_status_activity_fg:-default}
#     tmux_conf_theme_window_status_activity_bg=${tmux_conf_theme_window_status_activity_bg:-default}
#     tmux_conf_theme_window_status_activity_attr=${tmux_conf_theme_window_status_activity_attr:-underscore}
#
#     tmux_conf_theme_window_status_bell_fg=${tmux_conf_theme_window_status_bell_fg:-$tmux_conf_theme_colour_5}
#     tmux_conf_theme_window_status_bell_bg=${tmux_conf_theme_window_status_bell_bg:-default}
#     tmux_conf_theme_window_status_bell_attr=${tmux_conf_theme_window_status_bell_attr:-blink,bold}
#
#     tmux_conf_theme_window_status_last_fg=${tmux_conf_theme_window_status_last_fg:-$tmux_conf_theme_colour_4}
#     tmux_conf_theme_window_status_last_bg=${tmux_conf_theme_window_status_last_bg:-default}
#     tmux_conf_theme_window_status_last_attr=${tmux_conf_theme_window_status_last_attr:-none}
#
#     if [ "$tmux_conf_theme_window_status_bg" = "$tmux_conf_theme_status_bg" ] || [ "$tmux_conf_theme_window_status_bg" = "default" ]; then
#       spacer=''
#       spacer_current=' '
#     else
#       spacer=' '
#       spacer_current=' '
#     fi
#     if [ "$tmux_conf_theme_window_status_last_bg" = "$tmux_conf_theme_status_bg" ] || [ "$tmux_conf_theme_window_status_last_bg" = "default" ] ; then
#       spacer_last=''
#     else
#       spacer_last=' '
#     fi
#     if [ "$tmux_conf_theme_window_status_activity_bg" = "$tmux_conf_theme_status_bg" ] || [ "$tmux_conf_theme_window_status_activity_bg" = "default" ] ; then
#       spacer_activity=''
#       spacer_last_activity="$spacer_last"
#     else
#       spacer_activity=' '
#       spacer_last_activity=' '
#     fi
#     if [ "$tmux_conf_theme_window_status_bell_bg" = "$tmux_conf_theme_status_bg" ] || [ "$tmux_conf_theme_window_status_bell_bg" = "default" ] ; then
#       spacer_bell=''
#       spacer_last_bell="$spacer_last"
#       spacer_activity_bell="$spacer_activity"
#       spacer_last_activity_bell="$spacer_last_activity"
#     else
#       spacer_bell=' '
#       spacer_last_bell=' '
#       spacer_activity_bell=' '
#       spacer_last_activity_bell=' '
#     fi
#     spacer="#{?window_last_flag,#{?window_activity_flag,#{?window_bell_flag,$spacer_last_activity_bell,$spacer_last_activity},#{?window_bell_flag,$spacer_last_bell,$spacer_last}},#{?window_activity_flag,#{?window_bell_flag,$spacer_activity_bell,$spacer_activity},#{?window_bell_flag,$spacer_bell,$spacer}}}"
#     if [ "$(tmux show -g -v status-justify)" = "right" ]; then
#       if [ -z "$tmux_conf_theme_right_separator_main" ]; then
#         window_status_separator=' '
#       else
#         window_status_separator=''
#       fi
#       window_status_format="#[fg=$tmux_conf_theme_window_status_bg,bg=$tmux_conf_theme_status_bg,none]#{?window_last_flag,$(printf '%s' "$tmux_conf_theme_window_status_last_bg" | perl -n -e "s/.+/#[fg=$&]/; print if !/default/"),}#{?window_activity_flag,$(printf '%s' "$tmux_conf_theme_window_status_activity_bg" | perl -n -e "s/.+/#[fg=$&]/; print if !/default/"),}#{?window_bell_flag,$(printf '%s' "$tmux_conf_theme_window_status_bell_bg" | perl -n -e "s/.+/#[fg=$&]/; print if !/default/"),}$tmux_conf_theme_right_separator_main#[fg=$tmux_conf_theme_window_status_fg,bg=$tmux_conf_theme_window_status_bg,$tmux_conf_theme_window_status_attr]#{?window_last_flag,$(printf '%s' "$tmux_conf_theme_window_status_last_fg" | perl -n -e "s/.+/#[fg=$&]/; print if !/default/"),}#{?window_last_flag,$(printf '%s' "$tmux_conf_theme_window_status_last_bg" | perl -n -e "s/.+/#[bg=$&]/; print if !/default/"),}#{?window_activity_flag,$(printf '%s' "$tmux_conf_theme_window_status_activity_fg" | perl -n -e "s/.+/#[fg=$&]/; print if !/default/"),}#{?window_activity_flag,$(printf '%s' "$tmux_conf_theme_window_status_activity_bg" | perl -n -e "s/.+/#[bg=$&]/; print if !/default/"),}#{?window_bell_flag,$(printf '%s' "$tmux_conf_theme_window_status_bell_fg" | perl -n -e "s/.+/#[fg=$&]/; print if !/default/"),}#{?window_bell_flag,$(printf '%s' "$tmux_conf_theme_window_status_bell_bg" | perl -n -e "s/.+/#[bg=$&]/; print if !/default/"),}$spacer$(printf '%s' "$tmux_conf_theme_window_status_last_attr" | perl -n -e 'print "#{?window_last_flag,#[none],}" if !/default/ ; s/([a-z]+),?/#{?window_last_flag,#[\1],}/g; print if !/default/')$(printf '%s' "$tmux_conf_theme_window_status_activity_attr" | perl -n -e 'print "#{?window_activity_flag?,#[none],}" if !/default/ ; s/([a-z]+),?/#{?window_activity_flag,#[\1],}/g; print if !/default/')$(printf '%s' "$tmux_conf_theme_window_status_bell_attr" | perl -n -e 'print "#{?window_bell_flag,#[none],}" if !/default/ ; s/([a-z]+),?/#{?window_bell_flag,#[\1],}/g; print if !/default/')$tmux_conf_theme_window_status_format#[none]$spacer#[fg=$tmux_conf_theme_status_bg,bg=$tmux_conf_theme_window_status_bg]#{?window_last_flag,$(printf '%s' "$tmux_conf_theme_window_status_last_bg" | perl -n -e "s/.+/#[bg=$&]/; print if !/default/"),}#{?window_activity_flag,$(printf '%s' "$tmux_conf_theme_window_status_activity_bg" | perl -n -e "s/.+/#[bg=$&]/; print if !/default/"),}#{?window_bell_flag,$(printf '%s' "$tmux_conf_theme_window_status_bell_bg" | perl -n -e "s/.+/#[bg=$&]/; print if !/default/"),}#[none]$tmux_conf_theme_right_separator_main"
#       window_status_current_format="#[fg=$tmux_conf_theme_window_status_current_bg,bg=$tmux_conf_theme_status_bg,none]$tmux_conf_theme_right_separator_main#[fg=$tmux_conf_theme_window_status_current_fg,bg=$tmux_conf_theme_window_status_current_bg,$tmux_conf_theme_window_status_current_attr]$spacer_current$tmux_conf_theme_window_status_current_format$spacer_current#[fg=$tmux_conf_theme_status_bg,bg=$tmux_conf_theme_window_status_current_bg,none]$tmux_conf_theme_right_separator_main"
#     else
#       if [ -z "$tmux_conf_theme_left_separator_main" ]; then
#         window_status_separator=' '
#       else
#         window_status_separator=''
#       fi
#       window_status_format="#[fg=$tmux_conf_theme_status_bg,bg=$tmux_conf_theme_window_status_bg,none]#{?window_last_flag,$(printf '%s' "$tmux_conf_theme_window_status_last_bg" | perl -n -e "s/.+/#[bg=$&]/; print if !/default/"),}#{?window_activity_flag,$(printf '%s' "$tmux_conf_theme_window_status_activity_bg" | perl -n -e "s/.+/#[bg=$&]/; print if !/default/"),}#{?window_bell_flag,$(printf '%s' "$tmux_conf_theme_window_status_bell_bg" | perl -n -e "s/.+/#[bg=$&]/; print if !/default/"),}$tmux_conf_theme_left_separator_main#[fg=$tmux_conf_theme_window_status_fg,bg=$tmux_conf_theme_window_status_bg,$tmux_conf_theme_window_status_attr]#{?window_last_flag,$(printf '%s' "$tmux_conf_theme_window_status_last_fg" | perl -n -e "s/.+/#[fg=$&]/; print if !/default/"),}#{?window_last_flag,$(printf '%s' "$tmux_conf_theme_window_status_last_bg" | perl -n -e "s/.+/#[bg=$&]/; print if !/default/"),}#{?window_activity_flag,$(printf '%s' "$tmux_conf_theme_window_status_activity_fg" | perl -n -e "s/.+/#[fg=$&]/; print if !/default/"),}#{?window_activity_flag,$(printf '%s' "$tmux_conf_theme_window_status_activity_bg" | perl -n -e "s/.+/#[bg=$&]/; print if !/default/"),}#{?window_bell_flag,$(printf '%s' "$tmux_conf_theme_window_status_bell_fg" | perl -n -e "s/.+/#[fg=$&]/; print if !/default/"),}#{?window_bell_flag,$(printf '%s' "$tmux_conf_theme_window_status_bell_bg" | perl -n -e "s/.+/#[bg=$&]/; print if !/default/"),}$spacer$(printf '%s' "$tmux_conf_theme_window_status_last_attr" | perl -n -e 'print "#{?window_last_flag,#[none],}" if !/default/ ; s/([a-z]+),?/#{?window_last_flag,#[\1],}/g; print if !/default/')$(printf '%s' "$tmux_conf_theme_window_status_activity_attr" | perl -n -e 'print "#{?window_activity_flag,#[none],}" if !/default/ ; s/([a-z]+),?/#{?window_activity_flag,#[\1],}/g; print if !/default/')$(printf '%s' "$tmux_conf_theme_window_status_bell_attr" | perl -n -e 'print "#{?window_bell_flag,#[none],}" if /!default/ ; s/([a-z]+),?/#{?window_bell_flag,#[\1],}/g; print if !/default/')$tmux_conf_theme_window_status_format#[none]$spacer#[fg=$tmux_conf_theme_window_status_bg,bg=$tmux_conf_theme_status_bg]#{?window_last_flag,$(printf '%s' "$tmux_conf_theme_window_status_last_bg" | perl -n -e "s/.+/#[fg=$&]/; print if !/default/"),}#{?window_activity_flag,$(printf '%s' "$tmux_conf_theme_window_status_activity_bg" | perl -n -e "s/.+/#[fg=$&]/; print if !/default/"),}#{?window_bell_flag,$(printf '%s' "$tmux_conf_theme_window_status_bell_bg" | perl -n -e "s/.+/#[fg=$&]/; print if !/default/"),}$tmux_conf_theme_left_separator_main"
#       window_status_current_format="#[fg=$tmux_conf_theme_status_bg,bg=$tmux_conf_theme_window_status_current_bg,none]$tmux_conf_theme_left_separator_main#[fg=$tmux_conf_theme_window_status_current_fg,bg=$tmux_conf_theme_window_status_current_bg,$tmux_conf_theme_window_status_current_attr]$spacer_current$tmux_conf_theme_window_status_current_format$spacer_current#[fg=$tmux_conf_theme_window_status_current_bg,bg=$tmux_conf_theme_status_bg]$tmux_conf_theme_left_separator_main"
#     fi
#
#     # -- indicators
#
#     tmux_conf_theme_pairing=${tmux_conf_theme_pairing:-⚇}                         # U+2687
#     tmux_conf_theme_pairing_fg=${tmux_conf_theme_pairing_fg:-none}
#     tmux_conf_theme_pairing_bg=${tmux_conf_theme_pairing_bg:-none}
#     tmux_conf_theme_pairing_attr=${tmux_conf_theme_pairing_attr:-none}
#
#     tmux_conf_theme_prefix=${tmux_conf_theme_prefix:-⌨}                           # U+2328
#     tmux_conf_theme_prefix_fg=${tmux_conf_theme_prefix_fg:-none}
#     tmux_conf_theme_prefix_bg=${tmux_conf_theme_prefix_bg:-none}
#     tmux_conf_theme_prefix_attr=${tmux_conf_theme_prefix_attr:-none}
#
#     tmux_conf_theme_mouse=${tmux_conf_theme_mouse:-↗}                             # U+2197
#     tmux_conf_theme_mouse_fg=${tmux_conf_theme_mouse_fg:-none}
#     tmux_conf_theme_mouse_bg=${tmux_conf_theme_mouse_bg:-none}
#     tmux_conf_theme_mouse_attr=${tmux_conf_theme_mouse_attr:-none}
#
#     tmux_conf_theme_root=${tmux_conf_theme_root:-!}
#     tmux_conf_theme_root_fg=${tmux_conf_theme_root_fg:-none}
#     tmux_conf_theme_root_bg=${tmux_conf_theme_root_bg:-none}
#     tmux_conf_theme_root_attr=${tmux_conf_theme_root_attr:-bold,blink}
#
#     tmux_conf_theme_synchronized=${tmux_conf_theme_synchronized:-⚏}               # U+268F
#     tmux_conf_theme_synchronized_fg=${tmux_conf_theme_synchronized_fg:-none}
#     tmux_conf_theme_synchronized_bg=${tmux_conf_theme_synchronized_bg:-none}
#     tmux_conf_theme_synchronized_attr=${tmux_conf_theme_synchronized_attr:-none}
#
#     # -- status-left style
#
#     tmux_conf_theme_status_left=${tmux_conf_theme_status_left-' ❐ #S | ↑#{?uptime_y, #{uptime_y}y,}#{?uptime_d, #{uptime_d}d,}#{?uptime_h, #{uptime_h}h,}#{?uptime_m, #{uptime_m}m,} '}
#     tmux_conf_theme_status_left_fg=${tmux_conf_theme_status_left_fg:-$tmux_conf_theme_colour_6,$tmux_conf_theme_colour_7,$tmux_conf_theme_colour_8}
#     tmux_conf_theme_status_left_bg=${tmux_conf_theme_status_left_bg:-$tmux_conf_theme_colour_9,$tmux_conf_theme_colour_10,$tmux_conf_theme_colour_11}
#     tmux_conf_theme_status_left_attr=${tmux_conf_theme_status_left_attr:-bold,none,none}
#
#     if [ -n "$tmux_conf_theme_status_left" ]; then
#       status_left=$(echo "$tmux_conf_theme_status_left" | sed \
#         -e "s/#{pairing}/#[fg=$tmux_conf_theme_pairing_fg]#[bg=$tmux_conf_theme_pairing_bg]#[$tmux_conf_theme_pairing_attr]#{pairing}#[inherit]/g" \
#         -e "s/#{prefix}/#[fg=$tmux_conf_theme_prefix_fg]#[bg=$tmux_conf_theme_prefix_bg]#[$tmux_conf_theme_prefix_attr]#{prefix}#[inherit]/g" \
#         -e "s/#{mouse}/#[fg=$tmux_conf_theme_mouse_fg]#[bg=$tmux_conf_theme_mouse_bg]#[$tmux_conf_theme_mouse_attr]#{mouse}#[inherit]/g" \
#         -e "s/#{synchronized}/#[fg=$tmux_conf_theme_synchronized_fg]#[bg=$tmux_conf_theme_synchronized_bg]#[$tmux_conf_theme_synchronized_attr]#{synchronized}#[inherit]/g" \
#         -e "s/#{root}/#[fg=$tmux_conf_theme_root_fg]#[bg=$tmux_conf_theme_root_bg]#[$tmux_conf_theme_root_attr]#{root}#[inherit]/g")
#
#       status_left=$(printf '%s' "$status_left" | awk \
#                         -v status_bg="$tmux_conf_theme_status_bg" \
#                         -v fg_="$tmux_conf_theme_status_left_fg" \
#                         -v bg_="$tmux_conf_theme_status_left_bg" \
#                         -v attr_="$tmux_conf_theme_status_left_attr" \
#                         -v mainsep="$tmux_conf_theme_left_separator_main" \
#                         -v subsep="$tmux_conf_theme_left_separator_sub" '
#         function subsplit(s, l, i, a, r)
#         {
#           l = split(s, a, ",")
#           for (i = 1; i <= l; ++i)
#           {
#             o = split(a[i], _, "(") - 1
#             c = split(a[i], _, ")") - 1
#             open += o - c
#             o_ = split(a[i], _, "{") - 1
#             c_ = split(a[i], _, "}") - 1
#             open_ += o_ - c_
#             o__ = split(a[i], _, "[") - 1
#             c__ = split(a[i], _, "]") - 1
#             open__ += o__ - c__
#
#             if (i == l)
#               r = sprintf("%s%s", r, a[i])
#             else if (open || open_ || open__)
#               r = sprintf("%s%s,", r, a[i])
#             else
#               r = sprintf("%s%s#[fg=%s,bg=%s,%s]%s", r, a[i], fg[j], bg[j], attr[j], subsep)
#           }
#
#           gsub(/#\[inherit\]/, sprintf("#[default]#[fg=%s,bg=%s,%s]", fg[j], bg[j], attr[j]), r)
#           return r
#         }
#         BEGIN {
#           FS = "|"
#           l1 = split(fg_, fg, ",")
#           l2 = split(bg_, bg, ",")
#           l3 = split(attr_, attr, ",")
#           l = l1 < l2 ? (l1 < l3 ? l1 : l3) : (l2 < l3 ? l2 : l3)
#         }
#         {
#           for (i = j = 1; i <= NF; ++i)
#           {
#             if (open || open_ || open__)
#               printf "|%s", subsplit($i)
#             else
#             {
#               if (i > 1)
#                 printf "#[fg=%s,bg=%s,none]%s#[fg=%s,bg=%s,%s]%s", bg[j_], bg[j], mainsep, fg[j], bg[j], attr[j], subsplit($i)
#               else
#                 printf "#[fg=%s,bg=%s,%s]%s", fg[j], bg[j], attr[j], subsplit($i)
#             }
#
#             if (!open && !open_ && !open__)
#             {
#               j_ = j
#               j = j % l + 1
#             }
#           }
#           printf "#[fg=%s,bg=%s,none]%s", bg[j_], status_bg, mainsep
#         }')
#     fi
#     status_left="$status_left "
#
#     # -- status-right style
#
#     tmux_conf_theme_status_right=${tmux_conf_theme_status_right-' #{prefix}#{mouse}#{pairing}#{synchronized}#{?battery_status, #{battery_status},}#{?battery_bar, #{battery_bar},}#{?battery_percentage, #{battery_percentage},} , %R , %d %b | #{username}#{root} | #{hostname} '}
#     tmux_conf_theme_status_right_fg=${tmux_conf_theme_status_right_fg:-$tmux_conf_theme_colour_12,$tmux_conf_theme_colour_13,$tmux_conf_theme_colour_14}
#     tmux_conf_theme_status_right_bg=${tmux_conf_theme_status_right_bg:-$tmux_conf_theme_colour_15,$tmux_conf_theme_colour_16,$tmux_conf_theme_colour_17}
#     tmux_conf_theme_status_right_attr=${tmux_conf_theme_status_right_attr:-none,none,bold}
#
#     if [ -n "$tmux_conf_theme_status_right" ]; then
#       status_right=$(echo "$tmux_conf_theme_status_right" | sed \
#         -e "s/#{pairing}/#[fg=$tmux_conf_theme_pairing_fg]#[bg=$tmux_conf_theme_pairing_bg]#[$tmux_conf_theme_pairing_attr]#{pairing}#[inherit]/g" \
#         -e "s/#{prefix}/#[fg=$tmux_conf_theme_prefix_fg]#[bg=$tmux_conf_theme_prefix_bg]#[$tmux_conf_theme_prefix_attr]#{prefix}#[inherit]/g" \
#         -e "s/#{mouse}/#[fg=$tmux_conf_theme_mouse_fg]#[bg=$tmux_conf_theme_mouse_bg]#[$tmux_conf_theme_mouse_attr]#{mouse}#[inherit]/g" \
#         -e "s/#{synchronized}/#[fg=$tmux_conf_theme_synchronized_fg]#[bg=$tmux_conf_theme_synchronized_bg]#[$tmux_conf_theme_synchronized_attr]#{synchronized}#[inherit]/g" \
#         -e "s/#{root}/#[fg=$tmux_conf_theme_root_fg]#[bg=$tmux_conf_theme_root_bg]#[$tmux_conf_theme_root_attr]#{root}#[inherit]/g")
#
#       status_right=$(printf '%s' "$status_right" | awk \
#                         -v status_bg="$tmux_conf_theme_status_bg" \
#                         -v fg_="$tmux_conf_theme_status_right_fg" \
#                         -v bg_="$tmux_conf_theme_status_right_bg" \
#                         -v attr_="$tmux_conf_theme_status_right_attr" \
#                         -v mainsep="$tmux_conf_theme_right_separator_main" \
#                         -v subsep="$tmux_conf_theme_right_separator_sub" '
#         function subsplit(s, l, i, a, r)
#         {
#           l = split(s, a, ",")
#           for (i = 1; i <= l; ++i)
#           {
#             o = split(a[i], _, "(") - 1
#             c = split(a[i], _, ")") - 1
#             open += o - c
#             o_ = split(a[i], _, "{") - 1
#             c_ = split(a[i], _, "}") - 1
#             open_ += o_ - c_
#             o__ = split(a[i], _, "[") - 1
#             c__ = split(a[i], _, "]") - 1
#             open__ += o__ - c__
#
#             if (i == l)
#               r = sprintf("%s%s", r, a[i])
#             else if (open || open_ || open__)
#               r = sprintf("%s%s,", r, a[i])
#             else
#               r = sprintf("%s%s#[fg=%s,bg=%s,%s]%s", r, a[i], fg[j], bg[j], attr[j], subsep)
#           }
#
#           gsub(/#\[inherit\]/, sprintf("#[default]#[fg=%s,bg=%s,%s]", fg[j], bg[j], attr[j]), r)
#           return r
#         }
#         BEGIN {
#           FS = "|"
#           l1 = split(fg_, fg, ",")
#           l2 = split(bg_, bg, ",")
#           l3 = split(attr_, attr, ",")
#           l = l1 < l2 ? (l1 < l3 ? l1 : l3) : (l2 < l3 ? l2 : l3)
#         }
#         {
#           for (i = j = 1; i <= NF; ++i)
#           {
#             if (open_ || open || open__)
#               printf "|%s", subsplit($i)
#             else
#               printf "#[fg=%s,bg=%s,none]%s#[fg=%s,bg=%s,%s]%s", bg[j], (i == 1) ? status_bg : bg[j_], mainsep, fg[j], bg[j], attr[j], subsplit($i)
#
#             if (!open && !open_ && !open__)
#             {
#               j_ = j
#               j = j % l + 1
#             }
#           }
#         }')
#     fi
#     status_right=${status_right-}
#
#     # -- clock ---------------------------------------------------------------
#
#     tmux_conf_theme_clock_colour=${tmux_conf_theme_clock_colour:-$tmux_conf_theme_colour_4}
#     tmux_conf_theme_clock_style=${tmux_conf_theme_clock_style:-24}
#
#     tmux setw -g window-style "$window_style" \; setw -g window-active-style "$window_active_style" \;\
#          setw -g pane-border-style "fg=$tmux_conf_theme_pane_border_fg,bg=$tmux_conf_theme_pane_border_bg" \; set -g pane-active-border-style "fg=$tmux_conf_theme_pane_active_border_fg,bg=$tmux_conf_theme_pane_active_border_bg" \;\
#          set -g display-panes-colour "$tmux_conf_theme_pane_indicator" \; set -g display-panes-active-colour "$tmux_conf_theme_pane_active_indicator" \;\
#          set -g message-style "fg=$tmux_conf_theme_message_fg,bg=$tmux_conf_theme_message_bg,$tmux_conf_theme_message_attr" \;\
#          set -g message-command-style "fg=$tmux_conf_theme_message_command_fg,bg=$tmux_conf_theme_message_command_bg,$tmux_conf_theme_message_command_attr" \;\
#          setw -g mode-style "fg=$tmux_conf_theme_mode_fg,bg=$tmux_conf_theme_mode_bg,$tmux_conf_theme_mode_attr" \;\
#          set -g status-style "fg=$tmux_conf_theme_status_fg,bg=$tmux_conf_theme_status_bg,$tmux_conf_theme_status_attr" \;\
#          set -g status-left-style "fg=$tmux_conf_theme_status_fg,bg=$tmux_conf_theme_status_bg,$tmux_conf_theme_status_attr" \;\
#          set -g status-right-style "fg=$tmux_conf_theme_status_fg,bg=$tmux_conf_theme_status_bg,$tmux_conf_theme_status_attr" \;\
#          setw -g window-status-style "fg=$tmux_conf_theme_window_status_fg,bg=$tmux_conf_theme_window_status_bg,$tmux_conf_theme_window_status_attr" \;\
#          setw -g window-status-current-style "fg=$tmux_conf_theme_window_status_current_fg,bg=$tmux_conf_theme_window_status_current_bg,$tmux_conf_theme_window_status_current_attr" \;\
#          setw -g window-status-activity-style "fg=$tmux_conf_theme_window_status_activity_fg,bg=$tmux_conf_theme_window_status_activity_bg,$tmux_conf_theme_window_status_activity_attr" \;\
#          setw -g window-status-bell-style "fg=$tmux_conf_theme_window_status_bell_fg,bg=$tmux_conf_theme_window_status_bell_bg,$tmux_conf_theme_window_status_bell_attr" \;\
#          setw -g window-status-last-style "fg=$tmux_conf_theme_window_status_last_fg,bg=$tmux_conf_theme_window_status_last_bg,$tmux_conf_theme_window_status_last_attr" \;\
#          setw -g window-status-separator "$window_status_separator" \;\
#          setw -g clock-mode-colour "$tmux_conf_theme_clock_colour" \;\
#          setw -g clock-mode-style "$tmux_conf_theme_clock_style"
#   fi
#
#   # -- variables -------------------------------------------------------------
#
#   set_titles_string=$(printf '%s' "${tmux_conf_theme_terminal_title:-$(tmux show -gv set-titles-string)}" | sed \
#     -e "s%#{circled_window_index}%#(cut -c3- '$TMUX_CONF' | sh -s _circled '#I')%g" \
#     -e "s%#{circled_session_name}%#(cut -c3- '$TMUX_CONF' | sh -s _circled '#S')%g" \
#     -e "s%#{username}%#(cut -c3- '$TMUX_CONF' | sh -s _username '#{pane_pid}' '#{b:pane_tty}' false '#D')%g" \
#     -e "s%#{hostname}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' false false '#h' '#D')%g" \
#     -e "s%#{hostname_full}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' false true '#H' '#D')%g" \
#     -e "s%#{username_ssh}%#(cut -c3- '$TMUX_CONF' | sh -s _username '#{pane_pid}' '#{b:pane_tty}' true '#D')%g" \
#     -e "s%#{hostname_ssh}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' true false '#h' '#D')%g" \
#     -e "s%#{hostname_full_ssh}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' true true '#H' '#D')%g")
#
#   window_status_format=$(printf '%s' "${window_status_format:-$(tmux show -gv window-status-format)}" | sed \
#     -e "s%#{circled_window_index}%#(cut -c3- '$TMUX_CONF' | sh -s _circled '#I')%g" \
#     -e "s%#{circled_session_name}%#(cut -c3- '$TMUX_CONF' | sh -s _circled '#S')%g" \
#     -e "s%#{username}%#(cut -c3- '$TMUX_CONF' | sh -s _username '#{pane_pid}' '#{b:pane_tty}' false '#D')%g" \
#     -e "s%#{hostname}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' false false '#h' '#D')%g" \
#     -e "s%#{hostname_full}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' false true '#H' '#D')%g" \
#     -e "s%#{username_ssh}%#(cut -c3- '$TMUX_CONF' | sh -s _username '#{pane_pid}' '#{b:pane_tty}' true '#D')%g" \
#     -e "s%#{hostname_ssh}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' true false '#h' '#D')%g" \
#     -e "s%#{hostname_full_ssh}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' true true '#H' '#D')%g")
#
#   window_status_current_format=$(printf '%s' "${window_status_current_format:-$(tmux show -gv window-status-current-format)}" | sed \
#     -e "s%#{circled_window_index}%#(cut -c3- '$TMUX_CONF' | sh -s _circled '#I')%g" \
#     -e "s%#{circled_session_name}%#(cut -c3- '$TMUX_CONF' | sh -s _circled '#S')%g" \
#     -e "s%#{username}%#(cut -c3- '$TMUX_CONF' | sh -s _username '#{pane_pid}' '#{b:pane_tty}' false '#D')%g" \
#     -e "s%#{hostname}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' false false '#h' '#D')%g" \
#     -e "s%#{hostname_full}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' false true '#H' '#D')%g" \
#     -e "s%#{username_ssh}%#(cut -c3- '$TMUX_CONF' | sh -s _username '#{pane_pid}' '#{b:pane_tty}' true '#D')%g" \
#     -e "s%#{hostname_ssh}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' true false '#h' '#D')%g" \
#     -e "s%#{hostname_full_ssh}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' true true '#H' '#D')%g")
#
#   status_left=$(printf '%s' "${status_left-$(tmux show -gv status-left)}" | sed \
#     -e "s/#{pairing}/#{?session_many_attached,$tmux_conf_theme_pairing ,}/g" \
#     -e "s/#{prefix}/#{?client_prefix,$tmux_conf_theme_prefix ,$(printf '%s' "$tmux_conf_theme_prefix" | sed -e 's/./ /g') }/g" \
#     -e "s/#{mouse}/#{?mouse,$tmux_conf_theme_mouse ,$(printf '%s' "$tmux_conf_theme_mouse" | sed -e 's/./ /g') }/g" \
#     -e "s%#{synchronized}%#{?pane_synchronized,$tmux_conf_theme_synchronized ,}%g" \
#     -e "s%#{circled_session_name}%#(cut -c3- '$TMUX_CONF' | sh -s _circled '#S')%g" \
#     -e "s%#{root}%#{?#{==:#(cut -c3- '$TMUX_CONF' | sh -s _username '#{pane_pid}' '#{b:pane_tty}' '#D'),root},$tmux_conf_theme_root,}%g")
#
#   status_right=$(printf '%s' "${status_right-$(tmux show -gv status-right)}" | sed \
#     -e "s/#{pairing}/#{?session_many_attached,$tmux_conf_theme_pairing ,}/g" \
#     -e "s/#{prefix}/#{?client_prefix,$tmux_conf_theme_prefix ,$(printf '%s' "$tmux_conf_theme_prefix" | sed -e 's/./ /g') }/g" \
#     -e "s/#{mouse}/#{?mouse,$tmux_conf_theme_mouse ,$(printf '%s' "$tmux_conf_theme_mouse" | sed -e 's/./ /g') }/g" \
#     -e "s%#{synchronized}%#{?pane_synchronized,$tmux_conf_theme_synchronized ,}%g" \
#     -e "s%#{circled_session_name}%#(cut -c3- '$TMUX_CONF' | sh -s _circled '#S')%g" \
#     -e "s%#{root}%#{?#{==:#(cut -c3- '$TMUX_CONF' | sh -s _username '#{pane_pid}' '#{b:pane_tty}' '#D'),root},$tmux_conf_theme_root,}%g")
#
#   tmux_conf_battery_bar_symbol_full=$(_decode_unicode_escapes "${tmux_conf_battery_bar_symbol_full:-◼}")
#   tmux_conf_battery_bar_symbol_empty=$(_decode_unicode_escapes "${tmux_conf_battery_bar_symbol_empty:-◻}")
#   tmux_conf_battery_bar_length=${tmux_conf_battery_bar_length:-auto}
#   tmux_conf_battery_bar_palette=${tmux_conf_battery_bar_palette:-gradient}
#   tmux_conf_battery_hbar_palette=${tmux_conf_battery_hbar_palette:-gradient}
#   tmux_conf_battery_vbar_palette=${tmux_conf_battery_vbar_palette:-gradient}
#   tmux_conf_battery_status_charging=$(_decode_unicode_escapes "${tmux_conf_battery_status_charging:-↑}")        # U+2191
#   tmux_conf_battery_status_discharging=$(_decode_unicode_escapes "${tmux_conf_battery_status_discharging:-↓}")  # U+2193
#
#   _pkillf "cut -c3- '$TMUX_CONF' \| sh -s _battery"
#   _battery_info
#   if [ "$battery_charge" != 0 ]; then
#     case "$status_left $status_right" in
#       *'#{battery_'*|*'#{?battery_'*)
#         status_left=$(echo "$status_left" | sed -E \
#           -e 's%#\{\?battery_bar%#\{?@battery_percentage%g' \
#           -e 's%#\{\?battery_hbar%#\{?@battery_percentage%g' \
#           -e 's%#\{\?battery_vbar%#\{?@battery_percentage%g' \
#           -e "s%#\{battery_bar\}%#(nice cut -c3- '$TMUX_CONF' | sh -s _bar '$(printf '%s' "$tmux_conf_battery_bar_palette" | tr ',' ';')' '$tmux_conf_battery_bar_symbol_empty' '$tmux_conf_battery_bar_symbol_full' '$tmux_conf_battery_bar_length' '#{@battery_charge}' '#{client_width}')%g" \
#           -e "s%#\{battery_hbar\}%#(nice cut -c3- '$TMUX_CONF' | sh -s _hbar '$(printf '%s' "$tmux_conf_battery_hbar_palette" | tr ',' ';')' '#{@battery_charge}')%g" \
#           -e "s%#\{battery_vbar\}%#(nice cut -c3- '$TMUX_CONF' | sh -s _vbar '$(printf '%s' "$tmux_conf_battery_vbar_palette" | tr ',' ';')' '#{@battery_charge}')%g" \
#           -e 's%#\{(\?)?battery_status%#\{\1@battery_status%g' \
#           -e 's%#\{(\?)?battery_percentage%#\{\1@battery_percentage%g')
#         status_right=$(echo "$status_right" | sed -E \
#           -e 's%#\{\?battery_bar%#\{?@battery_percentage%g' \
#           -e 's%#\{\?battery_hbar%#\{?@battery_percentage%g' \
#           -e 's%#\{\?battery_vbar%#\{?@battery_percentage%g' \
#           -e "s%#\{battery_bar\}%#(nice cut -c3- '$TMUX_CONF' | sh -s _bar '$(printf '%s' "$tmux_conf_battery_bar_palette" | tr ',' ';')' '$tmux_conf_battery_bar_symbol_empty' '$tmux_conf_battery_bar_symbol_full' '$tmux_conf_battery_bar_length' '#{@battery_charge}' '#{client_width}')%g" \
#           -e "s%#\{battery_hbar\}%#(nice cut -c3- '$TMUX_CONF' | sh -s _hbar '$(printf '%s' "$tmux_conf_battery_hbar_palette" | tr ',' ';')' '#{@battery_charge}')%g" \
#           -e "s%#\{battery_vbar\}%#(nice cut -c3- '$TMUX_CONF' | sh -s _vbar '$(printf '%s' "$tmux_conf_battery_vbar_palette" | tr ',' ';')' '#{@battery_charge}')%g" \
#           -e 's%#\{(\?)?battery_status%#\{\1@battery_status%g' \
#           -e 's%#\{(\?)?battery_percentage%#\{\1@battery_percentage%g')
#         status_right="#(echo; nice cut -c3- '$TMUX_CONF' | sh -s _battery_status '$tmux_conf_battery_status_charging' '$tmux_conf_battery_status_discharging')$status_right"
#         interval=60
#         if [ "$_tmux_version" -ge 320 ]; then
#           tmux run -b "trap '[ -n \"\$sleep_pid\" ] && kill -9 \"\$sleep_pid\"; exit 0' TERM; while [ x\"\$('$TMUX_PROGRAM' -S '#{socket_path}' display -p '#{l:#{pid}}')\" = x\"#{pid}\" ]; do nice cut -c3- '$TMUX_CONF' | sh -s _battery_info; sleep $interval & sleep_pid=\$!; wait \"\$sleep_pid\"; sleep_pid=; done"
#         elif [ "$_tmux_version" -ge 280 ]; then
#           status_right="#(echo; while [ x\"\$('$TMUX_PROGRAM' -S '#{socket_path}' display -p '#{l:#{pid}}')\" = x\"#{pid}\" ]; do nice cut -c3- '$TMUX_CONF' | sh -s _battery_info; sleep $interval; done)$status_right"
#         elif [ "$_tmux_version" -gt 240 ]; then
#           status_right="#(echo; while :; do nice cut -c3- '$TMUX_CONF' | sh -s _battery_info; sleep $interval; done)$status_right"
#         else
#           status_right="#(nice cut -c3- '$TMUX_CONF' | sh -s _battery_info)$status_right"
#         fi
#         ;;
#     esac
#   fi
#
#   case "$status_left $status_right" in
#     *'#{username}'*|*'#{hostname}'*|*'#{hostname_full}'*|*'#{username_ssh}'*|*'#{hostname_ssh}'*|*'#{hostname_full_ssh}'*)
#       status_left=$(echo "$status_left" | sed \
#         -e "s%#{username}%#(cut -c3- '$TMUX_CONF' | sh -s _username '#{pane_pid}' '#{b:pane_tty}' false '#D')%g" \
#         -e "s%#{hostname}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' false false '#h' '#D')%g" \
#         -e "s%#{hostname_full}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' false true '#H' '#D')%g" \
#         -e "s%#{username_ssh}%#(cut -c3- '$TMUX_CONF' | sh -s _username '#{pane_pid}' '#{b:pane_tty}' true '#D')%g" \
#         -e "s%#{hostname_ssh}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' true false '#h' '#D')%g" \
#         -e "s%#{hostname_full_ssh}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' true true '#H' '#D')%g")
#       status_right=$(echo "$status_right" | sed \
#         -e "s%#{username}%#(cut -c3- '$TMUX_CONF' | sh -s _username '#{pane_pid}' '#{b:pane_tty}' false '#D')%g" \
#         -e "s%#{hostname}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' false false '#h' '#D')%g" \
#         -e "s%#{hostname_full}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' false true '#H' '#D')%g" \
#         -e "s%#{username_ssh}%#(cut -c3- '$TMUX_CONF' | sh -s _username '#{pane_pid}' '#{b:pane_tty}' true '#D')%g" \
#         -e "s%#{hostname_ssh}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' true false '#h' '#D')%g" \
#         -e "s%#{hostname_full_ssh}%#(cut -c3- '$TMUX_CONF' | sh -s _hostname '#{pane_pid}' '#{b:pane_tty}' true true '#H' '#D')%g")
#       ;;
#   esac
#
#   _pkillf "cut -c3- '$TMUX_CONF' \| sh -s _uptime"
#   case "$status_left $status_right" in
#     *'#{uptime_'*|*'#{?uptime_'*)
#       status_left=$(echo "$status_left" | perl -p -e '
#         ; s/#\{(\?)?uptime_y\b/#\{\1\@uptime_y/g
#         ; s/#\{(\?)?uptime_d\b/#\{\1\@uptime_d/g
#         ; s/\@uptime_d\b/\@uptime_dy/g if /\@uptime_y\b/
#         ; s/#\{(\?)?uptime_h\b/#\{\1\@uptime_h/g
#         ; s/#\{(\?)?uptime_m\b/#\{\1\@uptime_m/g
#         ; s/#\{(\?)?uptime_s\b/#\{\1\@uptime_s/g')
#       status_right=$(echo "$status_right" | perl -p -e '
#         ; s/#\{(\?)?uptime_y\b/#\{\1\@uptime_y/g
#         ; s/#\{(\?)?uptime_d\b/#\{\1\@uptime_d/g
#         ; s/\@uptime_d\b/\@uptime_dy/g if /\@uptime_y\b/
#         ; s/#\{(\?)?uptime_h\b/#\{\1\@uptime_h/g
#         ; s/#\{(\?)?uptime_m\b/#\{\1\@uptime_m/g
#         ; s/#\{(\?)?uptime_s\b/#\{\1\@uptime_s/g')
#       interval=60
#       case "$status_left $status_right" in
#         *'#{@uptime_s}'*)
#           interval=$(tmux show -gv status-interval)
#           ;;
#       esac
#       if [ "$_tmux_version" -ge 320 ]; then
#         tmux run -b "trap '[ -n \"\$sleep_pid\" ] && kill -9 \"\$sleep_pid\"; exit 0' TERM; while [ x\"\$('$TMUX_PROGRAM' -S '#{socket_path}' display -p '#{l:#{pid}}')\" = x\"#{pid}\" ]; do nice cut -c3- '$TMUX_CONF' | sh -s _uptime; sleep $interval & sleep_pid=\$!; wait \"\$sleep_pid\"; sleep_pid=; done"
#       elif [ "$_tmux_version" -ge 280 ]; then
#         status_right="#(echo; while [ x\"\$('$TMUX_PROGRAM' -S '#{socket_path}' display -p '#{l:#{pid}}')\" = x\"#{pid}\" ]; do nice cut -c3- '$TMUX_CONF' | sh -s _uptime; sleep $interval; done)$status_right"
#       elif [ "$_tmux_version" -gt 240 ]; then
#         status_right="#(echo; while :; do nice cut -c3- '$TMUX_CONF' | sh -s _uptime; sleep $interval; done)$status_right"
#       else
#         status_right="#(nice cut -c3- '$TMUX_CONF' | sh -s _uptime)$status_right"
#       fi
#       ;;
#   esac
#
#   _pkillf "cut -c3- '$TMUX_CONF' \| sh -s _loadavg"
#   case "$status_left $status_right" in
#     *'#{loadavg'*|*'#{?loadavg'*)
#       status_left=$(echo "$status_left" | sed -E \
#         -e 's/#\{(\?)?loadavg/#\{\1@loadavg/g')
#       status_right=$(echo "$status_right" | sed -E \
#         -e 's/#\{(\?)?loadavg/#\{\1@loadavg/g')
#       interval=$(tmux show -gv status-interval)
#       if [ "$_tmux_version" -ge 320 ]; then
#         tmux run -b "trap '[ -n \"\$sleep_pid\" ] && kill -9 \"\$sleep_pid\"; exit 0' TERM; while [ x\"\$('$TMUX_PROGRAM' -S '#{socket_path}' display -p '#{l:#{pid}}')\" = x\"#{pid}\" ]; do nice cut -c3- '$TMUX_CONF' | sh -s _loadavg; sleep $interval & sleep_pid=\$!; wait \"\$sleep_pid\"; sleep_pid=; done"
#       elif [ "$_tmux_version" -ge 280 ]; then
#         status_right="#(echo; while [ x\"\$('$TMUX_PROGRAM' -S '#{socket_path}' display -p '#{l:#{pid}}')\" = x\"#{pid}\" ]; do nice cut -c3- '$TMUX_CONF' | sh -s _loadavg; sleep $interval; done)$status_right"
#       elif [ "$_tmux_version" -gt 240 ]; then
#         status_right="#(echo; while :; do nice cut -c3- '$TMUX_CONF' | sh -s _loadavg; sleep $interval; done)$status_right"
#       else
#         status_right="#(nice cut -c3- '$TMUX_CONF' | sh -s _loadavg)$status_right"
#       fi
#       ;;
#   esac
#
#   # -- custom variables ------------------------------------------------------
#
#   if [ -f "$TMUX_CONF_LOCAL" ] && [ "$(cut -c3- "$TMUX_CONF_LOCAL" | sh 2>/dev/null -s printf probe)" = "probe" ]; then
#     replacements=$(perl -n -e 'print if s!^#\s+([^_][^()\s]+)\s*\(\)\s*{\s*(?:#.*)?\n!s%#\\\{\1((?:\\s+(?:[^\{\}]+?|#\\{(?:[^\{\}]+?)\}))*)\\\}%#(cut -c3- \"\\\$TMUX_CONF_LOCAL\" | sh -s \1\\1)%g; !p' "$TMUX_CONF_LOCAL")
#     status_left=$(echo "$status_left" | perl -p -e "$replacements" || echo "$status_left")
#     status_right=$(echo "$status_right" | perl -p -e "$replacements" || echo "$status_right")
#   fi
#
#   # --------------------------------------------------------------------------
#
#   tmux set -g set-titles-string "$(_decode_unicode_escapes "$set_titles_string")" \;\
#        setw -g window-status-format "$(_decode_unicode_escapes "$window_status_format")" \;\
#        setw -g window-status-current-format "$(_decode_unicode_escapes "$window_status_current_format")" \;\
#        set -g status-left-length 1000 \; set -g status-left "$(_decode_unicode_escapes "$status_left")" \;\
#        set -g status-right-length 1000 \; set -g status-right "$(_decode_unicode_escapes "$status_right")"
# }
#
# __apply_plugins() {
#   TMUX_PLUGIN_MANAGER_PATH="$1"
#   window_active="$2"
#   tmux_conf_update_plugins_on_launch="$3"
#   tmux_conf_update_plugins_on_reload="$4"
#   tmux_conf_uninstall_plugins_on_reload="$5"
#
#   if [ -z "$TMUX_PLUGIN_MANAGER_PATH" ]; then
#     return 255
#   fi
#   mkdir -p "$TMUX_PLUGIN_MANAGER_PATH"
#
#   tpm_plugins=$(tmux show -gvq '@tpm_plugins' 2>/dev/null)
#   if [ -z "$(tmux show -gv '@plugin' 2>/dev/null)" ] && [ -z "$tpm_plugins" ]; then
#     if _is_true "$tmux_conf_uninstall_plugins_on_reload" && [ -d "$TMUX_PLUGIN_MANAGER_PATH/tpm" ]; then
#       tmux display 'Uninstalling tpm and plugins...'
#       tmux set-environment -gu TMUX_PLUGIN_MANAGER_PATH
#       rm -rf "$TMUX_PLUGIN_MANAGER_PATH"
#       tmux display 'Done uninstalling tpm and plugins...'
#     fi
#   else
#     if [ "$(command tmux display -p '#{pid} #{version} #{socket_path}')" = "$($TMUX_PROGRAM display -p '#{pid} #{version} #{socket_path}')" ]; then
#       tpm_plugins=$(cat << EOF | tr ' ' '\n' | awk '/^\s*$/ {next;}; !seen[$0]++ { gsub(/^[ \t]+/,"",$0); gsub(/[ \t]+$/,"",$0); print $0 }'
#         $tpm_plugins
#         $(awk '/^[ \t]*set(-option)?.*[ \t]@plugin[ \t]/ { gsub(/'\''/, ""); gsub(/'\"'/, ""); print $NF }' "$TMUX_CONF_LOCAL" 2>/dev/null)
# EOF
#       )
#       tmux set-environment -g TMUX_PLUGIN_MANAGER_PATH "$TMUX_PLUGIN_MANAGER_PATH"
#       tmux set -g '@tpm_plugins' "$tpm_plugins"
#
#       if [ -d "$TMUX_PLUGIN_MANAGER_PATH/tpm" ]; then
#         [ -z "$(tmux show -gqv '@tpm-install')" ] && tmux set -g '@tpm-install' 'I'
#         [ -z "$(tmux show -gqv '@tpm-update')" ] && tmux set -g '@tpm-update' 'u'
#         [ -z "$(tmux show -gqv '@tpm-clean')" ] && tmux set -g '@tpm-clean' 'M-u'
#         "$TMUX_PLUGIN_MANAGER_PATH/tpm/tpm" || tmux display "One or more tpm plugin(s) failed"
#       fi
#
#       if git ls-remote -hq https://github.com/gpakosz/.tmux.git master > /dev/null; then
#         if [ ! -d "$TMUX_PLUGIN_MANAGER_PATH/tpm" ]; then
#           install_tpm=true
#           tmux display 'Installing tpm and plugins...'
#           git clone --depth 1 https://github.com/tmux-plugins/tpm "$TMUX_PLUGIN_MANAGER_PATH/tpm"
#         elif { [ -z "$window_active" ] && _is_true "$tmux_conf_update_plugins_on_launch"; } || { [ -n "$window_active" ] && _is_true "$tmux_conf_update_plugins_on_reload"; }; then
#           update_tpm=true
#           tmux display 'Updating tpm and plugins...'
#           (cd "$TMUX_PLUGIN_MANAGER_PATH/tpm" && git fetch -q -p && git checkout -q master && git reset -q --hard origin/master)
#         fi
#         if [ "$install_tpm" = "true" ] || [ "$update_tpm" = "true" ]; then
#           perl -0777 -p -i -e 's/git clone(?!\s+--depth\s+1)/git clone --depth 1/g
#                               ;s/(install_plugin(.(?!&))*)\n(\s+)done/\1&\n\3done\n\3wait/g' "$TMUX_PLUGIN_MANAGER_PATH/tpm/scripts/install_plugins.sh"
#           perl -p -i -e 's/git submodule update --init --recursive(?!\s+--depth\s+1)/git submodule update --init --recursive --depth 1/g' "$TMUX_PLUGIN_MANAGER_PATH/tpm/scripts/update_plugin.sh"
#           perl -p -i -e 's,\$tmux_file\s+>/dev/null\s+2>\&1,$& || { tmux display "Plugin \$(basename \${plugin_path}) failed" && false; },' "$TMUX_PLUGIN_MANAGER_PATH/tpm/scripts/source_plugins.sh"
#         fi
#         if [ "$update_tpm" = "true" ]; then
#           {
#             {
#               printf 'List of discovered tpm plugins: %s\n' "$(printf '%s\n' "$tpm_plugins" | paste -s -d ' ' -)" | perl -MPOSIX=strftime -MTime::HiRes=gettimeofday -pe 'my ($s, $us) = gettimeofday(); printf ("[%s.%03d]\t ", strftime("%Y-%m-%d %H:%M:%S", localtime $s), $us / 1000)'
#               printf '%s\n' "Invoking $TMUX_PLUGIN_MANAGER_PATH/tpm/bin/install_plugins" | perl -MPOSIX=strftime -MTime::HiRes=gettimeofday -pe 'my ($s, $us) = gettimeofday(); printf ("[%s.%03d]\t ", strftime("%Y-%m-%d %H:%M:%S", localtime $s), $us / 1000)'
#               "$TMUX_PLUGIN_MANAGER_PATH/tpm/bin/install_plugins" 2>&1 | perl -MPOSIX=strftime -MTime::HiRes=gettimeofday -pe 'my ($s, $us) = gettimeofday(); printf ("[%s.%03d]\t ", strftime("%Y-%m-%d %H:%M:%S", localtime $s), $us / 1000)'
#               printf '%s\n' "Invoking $TMUX_PLUGIN_MANAGER_PATH/tpm/bin/update_plugins all" | perl -MPOSIX=strftime -MTime::HiRes=gettimeofday -pe 'my ($s, $us) = gettimeofday(); printf ("[%s.%03d]\t ", strftime("%Y-%m-%d %H:%M:%S", localtime $s), $us / 1000)'
#               "$TMUX_PLUGIN_MANAGER_PATH/tpm/bin/update_plugins" all 2>&1 | perl -MPOSIX=strftime -MTime::HiRes=gettimeofday -pe 'my ($s, $us) = gettimeofday(); printf ("[%s.%03d]\t ", strftime("%Y-%m-%d %H:%M:%S", localtime $s), $us / 1000)'
#               printf '%s\n' "Invoking $TMUX_PLUGIN_MANAGER_PATH/tpm/bin/clean_plugins all" | perl -MPOSIX=strftime -MTime::HiRes=gettimeofday -pe 'my ($s, $us) = gettimeofday(); printf ("[%s.%03d]\t ", strftime("%Y-%m-%d %H:%M:%S", localtime $s), $us / 1000)'
#               "$TMUX_PLUGIN_MANAGER_PATH/tpm/bin/clean_plugins" all 2>&1 | perl -MPOSIX=strftime -MTime::HiRes=gettimeofday -pe 'my ($s, $us) = gettimeofday(); printf ("[%s.%03d]\t ", strftime("%Y-%m-%d %H:%M:%S", localtime $s), $us / 1000)'
#               printf 'Done.\n' | perl -MPOSIX=strftime -MTime::HiRes=gettimeofday -pe 'my ($s, $us) = gettimeofday(); printf ("[%s.%03d]\t ", strftime("%Y-%m-%d %H:%M:%S", localtime $s), $us / 1000)'
#               printf '\n'
#             } >> "$TMUX_PLUGIN_MANAGER_PATH/tpm_log.txt"
#
#             tmux display 'Done updating tpm and plugins...'
#           } || tmux display 'Failed updating tpm and plugins...'
#         elif [ "$install_tpm" = "true" ]; then
#           {
#             {
#               printf 'List of discovered tpm plugins: %s\n' "$(printf '%s\n' "$tpm_plugins" | paste -s -d ' ' -)" | perl -MPOSIX=strftime -MTime::HiRes=gettimeofday -pe 'my ($s, $us) = gettimeofday(); printf ("[%s.%03d]\t ", strftime("%Y-%m-%d %H:%M:%S", localtime $s), $us / 1000)'
#               printf '%s\n' "Invoking $TMUX_PLUGIN_MANAGER_PATH/tpm/bin/install_plugins" | perl -MPOSIX=strftime -MTime::HiRes=gettimeofday -pe 'my ($s, $us) = gettimeofday(); printf ("[%s.%03d]\t ", strftime("%Y-%m-%d %H:%M:%S", localtime $s), $us / 1000)'
#               "$TMUX_PLUGIN_MANAGER_PATH/tpm/bin/install_plugins" 2>&1 | perl -MPOSIX=strftime -MTime::HiRes=gettimeofday -pe 'my ($s, $us) = gettimeofday(); printf ("[%s.%03d]\t ", strftime("%Y-%m-%d %H:%M:%S", localtime $s), $us / 1000)'
#               printf 'Done.\n' | perl -MPOSIX=strftime -MTime::HiRes=gettimeofday -pe 'my ($s, $us) = gettimeofday(); printf ("[%s.%03d]\t ", strftime("%Y-%m-%d %H:%M:%S", localtime $s), $us / 1000)'
#               printf '\n' >> "$TMUX_PLUGIN_MANAGER_PATH/tpm_log.txt"
#             } >> "$TMUX_PLUGIN_MANAGER_PATH/tpm_log.txt"
#
#             tmux display 'Done installing tpm and plugins...'
#
#             [ -z "$(tmux show -gqv '@tpm-install')" ] && tmux set -g '@tpm-install' 'I'
#             [ -z "$(tmux show -gqv '@tpm-update')" ] && tmux set -g '@tpm-update' 'u'
#             [ -z "$(tmux show -gqv '@tpm-clean')" ] && tmux set -g '@tpm-clean' 'M-u'
#             "$TMUX_PLUGIN_MANAGER_PATH/tpm/tpm" || tmux display "One or more tpm plugin(s) failed"
#           } || tmux display 'Failed installing tpm and plugins...'
#         fi
#       else
#         tmux display "GitHub doesn't seem to be reachable, skipping installing and/or updating tpm and plugins..."
#       fi
#     else
#       tmux run -b "sleep \$((#{display-time} / 1000)) && '$TMUX_PROGRAM' set display-time 3000 \; display 'Cannot use tpm which assumes a globally installed tmux' \; set -u display-time"
#     fi
#
#     if [ "$_tmux_version" -gt 260 ]; then
#       tmux set -gu '@tpm-install' \; set -gu '@tpm-update' \; set -gu '@tpm-clean' \; set -gu '@plugin' \; set -gu '@tpm_plugins'
#     else
#       tmux set -g '@tpm-install' '' \; set -g '@tpm-update' '' \; set -g '@tpm-clean' '' \; set -g '@plugin' '' \; set-gu '@tpm_plugins' ''
#     fi
#   fi
# }
#
# _apply_plugins() {
#   tmux_conf_update_plugins_on_launch=${tmux_conf_update_plugins_on_launch:-true}
#   tmux_conf_update_plugins_on_reload=${tmux_conf_update_plugins_on_reload:-true}
#   tmux_conf_uninstall_plugins_on_reload=${tmux_conf_uninstall_plugins_on_reload:-true}
#
#   if [ -z "$TMUX_PLUGIN_MANAGER_PATH" ]; then
#     if [ "$(dirname "$TMUX_CONF")" = "$HOME" ]; then
#       TMUX_PLUGIN_MANAGER_PATH="$HOME/.tmux/plugins"
#     else
#       TMUX_PLUGIN_MANAGER_PATH="$(dirname "$TMUX_CONF")/plugins"
#     fi
#   fi
#   tmux run -b "cut -c3- '$TMUX_CONF' | sh -s __apply_plugins '$TMUX_PLUGIN_MANAGER_PATH' '$window_active' '$tmux_conf_update_plugins_on_launch' '$tmux_conf_update_plugins_on_reload' '$tmux_conf_uninstall_plugins_on_reload'"
# }
#
# _apply_important() {
#   cfg=$(mktemp) && trap 'rm -f $cfg*' EXIT
#
#   if perl -n -e 'print if /^\s*(?:set|bind|unbind).+?#!important\s*$/' "$TMUX_CONF_LOCAL" 2>/dev/null > "$cfg.local"; then
#     if ! tmux source-file "$cfg.local"; then
#       if tmux source-file -v /dev/null 2> /dev/null; then
#         verbose_flag='-v'
#       fi
#       while ! out=$(tmux source-file "${verbose_flag:+$verbose_flag}" "$cfg.local"); do
#         line=$(printf "%s" "$out" | tail -1 | cut -d':' -f2)
#         perl -n -i -e "if ($. != $line) { print }" "$cfg.local"
#       done
#     fi
#   fi
# }
#
# _apply_configuration() {
#   window_active="$(tmux display -p '#{window_active}' 2>/dev/null || true)"
#   if [ -z "$window_active" ]; then
#     if ! command -v perl > /dev/null 2>&1; then
#       tmux run -b 'tmux set display-time 3000 \; display "This configuration requires perl" \; set -u display-time \; run "sleep 3" \; kill-server'
#       return
#     fi
#     if ! perl -MTime::HiRes -e1 > /dev/null 2>&1; then
#       tmux run -b 'tmux set display-time 3000 \; display "This configuration requires perl Time::HiRes" \; set -u display-time \; run "sleep 3" \; kill-server'
#       return
#     fi
#     if ! command -v sed > /dev/null 2>&1; then
#       tmux run -b 'tmux set display-time 3000 \; display "This configuration requires sed" \; set -u display-time \; run "sleep 3" \; kill-server'
#       return
#     fi
#     if ! command -v awk > /dev/null 2>&1; then
#       tmux run -b 'tmux set display-time 3000 \; display "This configuration requires awk" \; set -u display-time \; run "sleep 3" \; kill-server'
#       return
#     fi
#     if [ "$_tmux_version" -lt 260 ]; then
#       tmux run -b 'tmux set display-time 3000 \; display "This configuration requires tmux 2.6+" \; set -u display-time \; run "sleep 3" \; kill-server'
#       return
#     fi
#   fi
#
#   case "$_uname_s" in
#     *CYGWIN*|*MSYS*)
#       # prevent Cygwin and MSYS2 from cd-ing into home directory when evaluating /etc/profile
#       tmux setenv -g CHERE_INVOKING 1
#       ;;
#   esac
#
#   _apply_tmux_256color
#   _apply_24b&
#   _apply_theme&
#   _apply_bindings&
#   wait
#
#   _apply_plugins
#   _apply_important
#
#   # shellcheck disable=SC2046
#   tmux setenv -gu tmux_conf_dummy $(printenv | grep -E -o '^tmux_conf_[^=]+' | awk '{printf "; setenv -gu %s", $0}')
# }
#
# _urlview() {
#   pane_id="$1"; shift
#   tmux capture-pane -J -S - -E - -b "urlview-$pane_id" -t "$pane_id"
#   tmux split-window "'$TMUX_PROGRAM' ${TMUX_SOCKET:+-S "$TMUX_SOCKET"} show-buffer -b 'urlview-$pane_id' | urlview || true; '$TMUX_PROGRAM' ${TMUX_SOCKET:+-S "$TMUX_SOCKET"} delete-buffer -b 'urlview-$pane_id'"
# }
#
# _urlscan() {
#   pane_id="$1"; shift
#   tmux capture-pane -J -S - -E - -b "urlscan-$pane_id" -t "$pane_id"
#   tmux split-window "'$TMUX_PROGRAM' ${TMUX_SOCKET:+-S "$TMUX_SOCKET"} show-buffer -b 'urlscan-$pane_id' | urlscan $* || true; '$TMUX_PROGRAM' ${TMUX_SOCKET:+-S "$TMUX_SOCKET"} delete-buffer -b 'urlscan-$pane_id'"
# }
#
# _fpp() {
#   tmux capture-pane -J -S - -E - -b "fpp-$1" -t "$1"
#   tmux split-window -c "$2" "'$TMUX_PROGRAM' ${TMUX_SOCKET:+-S "$TMUX_SOCKET"} show-buffer -b 'fpp-$1' | fpp || true; '$TMUX_PROGRAM' ${TMUX_SOCKET:+-S "$TMUX_SOCKET"} delete-buffer -b 'fpp-$1'"
# }
#
# "$@"
###########
```