import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Veendu, et see on õige tee
import 'boxicons';



const app = createApp(App);
app.use(router);
app.mount('#app');
