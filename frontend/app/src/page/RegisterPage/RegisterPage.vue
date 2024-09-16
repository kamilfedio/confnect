<template>
  <div>
    <AuthBackground />
    <div class="registerPage">
      <div class="registerPage__registerForm registerForm">
        <p v-if="emailError.value" class="registerForm__text">
          NIce to see you! We hope you will find everything you need here!
        </p>
        <form @submit.prevent="submitForm" class="registerForm__form">
          <input
            type="email"
            class="registerForm__input"
            placeholder="email"
            v-model="email"
            required
          />
          <input
            type="text"
            class="registerForm__input"
            placeholder="name"
            v-model="name"
            pattern="[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż]+ [A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż]+"
            title="Full name must consist of two words (first and last name), separated by a space."
            required
          />
          <input
            type="password"
            class="registerForm__input"
            placeholder="password"
            v-model="password"
            pattern="(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{7,}"
            title="Password must be at least 7 characters long, contain one uppercase letter and one digit."
            required
          />
          <div class="registerForm__checkboxContainer">
            <input
              type="checkbox"
              class="registerForm__input"
              id="rules"
              v-model="acceptRules"
              required
            />
            <label for="rules" class="registerForm__label">Accept rules</label>
          </div>
          <button type="submit" class="registerForm__btn">Get started</button>
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
