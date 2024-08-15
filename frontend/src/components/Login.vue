<template>
    <div class="login-page">
      <div class="content-box">
        <router-link to="/" class="back-icon">
        <box-icon name='arrow-back' color='#2d2c2c' size="1.4rem"></box-icon>
        <p class="back-text">back</p>
      </router-link>
        <div class="form">
          <form @submit.prevent="handleLogin">
          <div class="form-group">
            <label for="username">Username</label>
            <input type="text" id="username" v-model="username" required />
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" v-model="password" required />
          </div>
          <button type="submit" class="login-button">Login</button>
          <div class="footer-text">
            <span class="text-default">Don’t have an account?</span>
            <span class="text-hover">
              <router-link to="/signup" class="sign-up-link">No worries, Sign Up</router-link>
            </span>
          </div>
        </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "UserLogin",
    data() {
      return {
        username: '',
        password: ''
      };
    },
    methods: {
      handleLogin() {
        console.log('Logging in with:', this.username, this.password);
      }
    }
    
  };
  </script>
  
  <style scoped>
    @font-face {
      font-family: 'Pilowlava-Regular';
      src: url('@/assets/fonts/Pilowlava-Regular.otf') format('opentype');
      font-weight: normal;
      font-style: normal;
    }
  
    .login-page {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
  
    h1 {
      font-family: "Pilowlava-Regular", sans-serif;
      font-size: clamp(1.5rem, 5vw, 3.5rem);
      margin-bottom: 30px;
    }

    p {
      padding: 0;
      margin: 0;
      font-size: 0.9rem;
    }

  
  
    .content-box {
      display: flex;
      flex-direction: column;
      background-color: #0B0B0B;
      color: #ffffff;
      padding: 30px 30px 0px 30px;
      border-radius: 5px;
      text-align: center;
      max-width: 400px;
      width: 75%;
      box-shadow: 0 0 50px black;
    }

    .back-icon{
      display: flex;
      flex-direction: row;
      align-items: center;
      gap: 5px;
      color: #2D2C2C;
      text-decoration: none;
    }



    .form{
      padding: 25px;
    }
  
    .form-group {
      margin-bottom: 20px;
      text-align: left;
    }
  
    .form-group label {
      display: block;
      font-size: 0.9rem;
      margin-bottom: 1.3rem;
      color: #ABF335;
    }
  
    .form-group input {
      width: 100%;
      padding: 13px;
      border-radius: 5px;
      background-color: #171717;
      border: 1px #171717 solid;
      color: #B9B9B9;
      box-sizing: border-box;
      box-shadow: none; 
      outline: none; 
    }
    .form-group input:focus {
      border-color: #ABF335; 
      background-color: #2B2B2B; 
      transition: background-color 0.5s, transform 0.5s;
    }
  
    .login-button {
      display: block;
      width: 25%;
      padding: 10px;
      margin-top: 25px;
      border-radius: 5px;
      background-color: #171717;
      color: #ABF335;
      border: none;
      font-size: 0.9rem;
      cursor: pointer;
      transition: background-color 0.3s, transform 0.3s;

    }
    .login-button:hover {
      transform: scale(1.1);
    }
  
  .footer-text {
  position: relative;
  margin-top: 35px;
  padding-top: 35px;
  color: #2D2C2C;
  overflow: hidden;
}

.text-default, .text-hover {
  display: block;
  position: absolute;
  width: 100%;
  top: 0;
  left: 0;
  text-align: center;
  transition: opacity 0.35s linear, transform 0.75s cubic-bezier(0.645, 0.045, 0.355, 1);
}

.text-hover {
  opacity: 0;
  transform: translateY(20px);
}

.footer-text:hover .text-default {
  opacity: 0;
  transform: translateY(-20px);
}

.footer-text:hover .text-hover {
  opacity: 1;
  transform: translateY(0);
}

.sign-up-link {
  color: #ABF335;
  text-decoration: none;
  font-weight: bold;
}

.sign-up-link:hover {
  text-decoration: underline;
}
  </style>
  
