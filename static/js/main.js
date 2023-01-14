const { createApp } = Vue
const { createVuetify } = Vuetify

const vuetify = createVuetify()

const app = createApp({
    data  : () => ({
        cls : 'Selamat datang di Botlepy framework dengan Vuetify 3',
        aspectRatio : 16 / 9,
        width: 60,
    }),
})

app.use(vuetify).mount('#app')