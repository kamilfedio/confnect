<template>
  <div>
    <AuthBackground />
    <div class="registerPage">
      <div class="registerPage__registerForm registerForm">
        <p class="registerForm__text">
          NIce to see you! We hope you will find everything you need here!
        </p>
        <form action="sumbit" class="registerForm__form">
          <input type="email" class="registerForm__input" placeholder="email" />
          <input type="text" class="registerForm__input" placeholder="name" />
          <input type="password" class="registerForm__input" placeholder="password" />
          <div class="registerForm__checkboxContainer">
            <input type="checkbox" class="registerForm__input" id="rules" />
            <label for="rules" class="registerForm__label">Accept rules</label>
          </div>
          <button class="registerForm__btn">Get started</button>
        </form>
      </div>
      <div class="registerPage__logo logo">
        <img src="../../img/whiteBlueLogo.png" alt="" />
      </div>
      <div class="registerPage__btn" @click="goToLogin">login</div>
      <div class="registerPage__image">
        <div class="registerPage__part"></div>
      </div>
    </div>
  </div>
</template>

<script src="./RegisterPage.vue.ts"></script>
<style src="./RegisterPage.scss" scoped></style>
