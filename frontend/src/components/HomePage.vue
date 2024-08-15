<template>
  <div class="home-page">
    <div class="content-box">
      <h1><span>Money</span></h1>
      <h1><span>Tracker</span></h1>

      <p>Please choose an option:</p>
      <div class="links">
        <router-link to="/login" class="link-button chronicle-button">
          <span><em>Login</em></span>
          <span><em>Sign In</em></span>
        </router-link>
        <router-link to="/signup" class="link-button chronicle-button">
          <span><em>Sign Up</em></span>
          <span><em>Register</em></span>
        </router-link>
      </div>
      <p class="box-footer-text">Built by two engineers</p>
    </div>
  </div>
</template>
  
  <script>
  export default {
    name: "HomePage",
  };


  </script>
  
  <style scoped>

@font-face {
  font-family: 'Pilowlava-Regular';
  src: url('@/assets/fonts/Pilowlava-Regular.otf') format('opentype');
  font-weight: normal;
  font-style: normal;
}

.home-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

h1 {
  font-family: "Pilowlava-Regular", sans-serif;
  font-size: clamp(2.3rem, 5vw, 3.5rem);
  margin-bottom: 0;
  margin-top: 0;
}

p {
  margin-top: 50px;
  margin-bottom: 0px;
  padding: 0;
  color: #ffffff;
  font-size: 0.95rem;
}

.content-box {
  background-color: #0B0B0B;
  color: #ffffff;
  padding: 50px;
  border-radius: 8px;
  text-align: center;
  max-width: 75%;
  box-shadow: 0 0 50px black;
}

.links {
  margin-top: 32px;
  display: flex;
  gap: 20px;
  justify-content: center;
}

.link-button {
  text-decoration: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow: hidden;
  line-height: 1;
  border-radius: 5px;
  padding: clamp(10px, 2vw, 17px) clamp(15px, 3vw, 20px);
  cursor: pointer;
  border: none;
  background-color: #D9D9D9;
  color: #000000;
  font-weight: 550;
  width: 100%;
  font-size: clamp(0.5rem, 2.5vw, 1.2rem);
  transition: background 0.3s linear;
  will-change: background;
}

.link-button:hover {
  background: #ABF335;
}

.link-button:hover span:nth-of-type(1) em {
  opacity: 0;
  transform: rotateX(90deg) scaleX(0.9) translate3d(0, -10px, 0);
}

.link-button:hover span:nth-of-type(2) em {
  opacity: 1;
  transform: rotateX(0deg) scaleX(1) translateZ(0);
  transition: transform 0.75s cubic-bezier(0.645, 0.045, 0.355, 1), opacity 0.35s linear 0.3s;
}

span {
  position: relative;
  display: block;
  perspective: 108px;
}

span:nth-of-type(2) {
  position: absolute;
}

em {
  font-style: normal;
  display: inline-block;
  font-size: 1rem;
  color: black;
  font-weight: 600;
  will-change: transform, opacity, transition;
  transition: transform 0.55s cubic-bezier(0.645, 0.045, 0.355, 1), opacity 0.35s linear 0.2s;
}

span:nth-of-type(1) em {
  transform-origin: top;
}

span:nth-of-type(2) em {
  opacity: 0;
  transform: rotateX(-90deg) scaleX(0.9) translate3d(0, 10px, 0);
  transform-origin: bottom;
}

p.box-footer-text {
  color: #2D2C2C;
}


@media (max-width: 768px) {
  .links {
    flex-direction: column; 
    gap: 12px;
  }

  .link-button {
    width: 80%;
    padding: 15px 25px; 
    font-size: 1.5rem; 
  }
}

</style>
