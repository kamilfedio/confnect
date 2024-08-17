<template>
  <header>
    <div class="header">
      <div class="header__brand">Confnect</div>
      <div class="header__nav">
        <LandingPageNavigationVue />
      </div>
      <div class="header__login">
        <button class="header__btn">login</button>
      </div>
    </div>
  </header>
  <main>
    <section class="introduction">
      <p class="introduction__slogan">
        Are you bored with your usual presentations? Or maybe you want to clear up the mess of a
        rain of questions? We have something for you!
      </p>
      <div class="introduction__icon"></div>
      <div class="introduction__logo">
        <img src="../img/transparentBgc_logo.png" alt="brand logo" class="introduction__img" />
      </div>
      <p class="introduction__text">Your assistant in presentations</p>
      <button class="introduction__btn">Get started</button>
    </section>
    <section class="checkUs">
      <div class="checkUs__title">
        <img src="../img/line.png" alt="line" class="checkUs__img" />
        <p>Check us below!</p>
        <img src="../img/line.png" alt="line" class="checkUs__img" />
      </div>
      <div class="checkUs__screens screens">
        <div class="screens__item">
          <img src="../img/screen1.png" alt="screen1" class="screens__img" />
        </div>
        <div class="screens__item">
          <img src="../img/screen2.png" alt="screen2" class="screens__img" />
        </div>
        <div class="screens__item">
          <img src="../img/screen3.png" alt="screen3" class="screens__img" />
        </div>
      </div>
      <p class="checkUs__text">Screens from confnect</p>
    </section>
    <section class="feature">
      <h1 class="feature__title">Find your feature</h1>
      <div class="feature__blocks">
        <div class="feature__block">possibilities</div>
        <div class="feature__block">features</div>
        <div class="feature__block">needs</div>
        <div class="feature__block">description</div>
        <div class="feature__block">check out</div>
      </div>
      <div class="feature__images">
        <div class="feature__img">
          <img src="../img/features1.png" alt="features1" />
          <p>Live questions</p>
        </div>
        <div class="feature__img">
          <img src="../img/features2.png" alt="features2" />
          <p>Feedback</p>
        </div>
        <div class="feature__img">
          <img src="../img/features3.png" alt="features3" />
          <p>Notification</p>
        </div>
      </div>
    </section>
    <section class="journay">
      <h1 class="journay__title">Read something about our journay</h1>
      <div class="journay__blocks">
        <div class="journay__block">about us</div>
        <div class="journay__block">journay</div>
        <div class="journay__block">passion</div>
        <div class="journay__block">description</div>
        <div class="journay__block">meet us</div>
      </div>
      <div class="journay__text">
        Lorem ipsum dolor sit amet consectetur adipiscing elit Ut et massa mi. Aliquam in hendrerit
        urna. Pellentesque sit amet sapien fringilla, mattis ligula consectetur, ultrices mauris.
        Maecenas vitae mattis tellus. Nullam quis imperdiet augue. Vestibulum auctor ornare leo, non
        suscipit.
      </div>
    </section>
    <section class="writeToUs">
      <h1 class="writeToUs__title">Write to us</h1>
      <div class="writeToUs__blocks">
        <div class="writeToUs__block">questions</div>
        <div class="writeToUs__block">contact</div>
        <div class="writeToUs__block">what's up</div>
        <div class="writeToUs__block">close to us</div>
        <div class="writeToUs__block">issue?</div>
      </div>
      <div class="writeToUs__text">
        If you meet any issue or want to us about something directly - fill in our form! We will
        reply as fast as possible
      </div>
      <div class="contactForm">
        <textarea class="contactForm__textArea" placeholder="Your issue..."></textarea>
        <div class="contactForm__details">
          <h1 class="contactForm__title">Contact Form</h1>
          <input type="text" class="contactForm__input" placeholder="Your email..." />
          <input type="text" class="contactForm__input" placeholder="Your name..." />
          <button class="contactForm__btn">Send</button>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup lang="ts">
import LandingPageNavigationVue from '../components/LandingPageNavigation.vue'
</script>

<style lang="scss">
header {
  height: 10vh;
}

.header {
  display: flex;
  align-items: flex-end;
  width: 100%;
  height: 50px;
  padding: 70px 0 50px 0;

  &__brand {
    font-size: 2.4em;
    padding: 0 100px 0 10px;
  }

  &__nav {
    flex-grow: 2;
  }

  &__login {
    padding: 0 10px;
  }
  &__btn {
    font-size: 1.3em;
    width: 87px;
    height: 30px;
    color: $mainDarkBlue;
    border: 1px solid $mainBlack;
    border-radius: 20px;
  }
}

main {
  .introduction {
    width: 60%;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    &__slogan {
      font-size: 2.4em;
      text-align: center;
      margin-top: 120px;
      letter-spacing: 1px;
    }
    &__logo {
      margin: 0 auto;
      margin-top: 140px;
    }
    &__text {
      text-align: center;
      font-size: 2em;
      margin-top: 20px;
    }
    &__btn {
      font-size: 1.6em;
      width: 195px;
      height: 45px;
      color: $mainDarkBlue;
      border: 2px solid $mainDarkBlue;
      border-radius: 20px;
      margin: 0 auto;
      margin-top: 80px;
    }
  }
  .checkUs {
    margin-top: 160px;

    &__title {
      font-size: 1.4em;
      text-align: center;
      display: flex;
      justify-content: center;
      align-items: center;
      p {
        margin: 0 8px;
      }
    }
    &__screens {
      margin-top: 40px;
      &.screens {
        padding: 40px;
        padding-bottom: 0;
        display: flex;
        justify-content: space-between;
      }
    }
    &__text {
      font-size: 1.2em;
      padding: 10px;
      text-align: center;
      color: $mainDarkBlue;
    }
  }
  .feature,
  .journay,
  .writeToUs {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 140px;
    &__title {
      font-size: 4em;
      color: $mainDarkBlue;
      font-weight: normal;
      padding-bottom: 30px;
    }
    &__blocks {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-evenly;
    }
    &__block {
      flex-basis: 30%;
      font-size: 1.2em;
      font-weight: normal;
      text-align: center;
      color: $mainDarkBlue;
      background-color: $lightGrey;
      border-radius: 20px;
      padding: 6px 12px;
      margin: 6px 0;
      letter-spacing: 1px;
    }
    &__images {
      display: flex;
      justify-content: space-between;
      margin-top: 80px;
      width: 65%;
      font-size: 1.6em;
      color: $mainDarkBlue;
      text-align: center;
    }
    &__img p {
      padding: 10px 0;
    }
  }
  .features {
    &__images {
      display: flex;
      justify-content: space-between;
      margin-top: 80px;
      width: 65%;
      font-size: 1.6em;
      color: $mainDarkBlue;
      text-align: center;
    }
    &__img p {
      padding: 10px 0;
    }
  }
  .journay,
  .writeToUs {
    &__text {
      font-size: 1.8em;
      width: 52%;
      text-align: center;
      margin-top: 40px;
      letter-spacing: 1px;
      line-height: 1.8em;
    }
    .contactForm {
      margin: 50px 0;
      display: flex;
      justify-content: space-between;
      width: 55%;
      &__textArea {
        background-color: $lightGrey;
        padding: 20px;
        border: none;
        border-radius: 20px;
        width: 344px;
        height: 214px;
        box-shadow: -6px -6px 0 0 $mainDarkBlue;
        font-size: 1.2em;
        &::placeholder {
          color: $mainDarkBlue;
        }
      }
      &__details {
        display: flex;
        flex-direction: column;
        padding: 20px;
        width: 40%;
      }
      &__title {
        font-size: 2.4em;
        color: $mainDarkBlue;
        font-weight: normal;
        padding-bottom: 50px;
      }
      &__input {
        background-color: transparent;
        border: none;
        border-bottom: 1px solid black;
        font-size: 1em;
        padding-bottom: 5px;
        margin-bottom: 10px;
        &::placeholder {
          color: $mainDarkBlue;
        }
      }
      &__btn {
        font-size: 13px;
        border: 1px solid $mainDarkBlue;
        border-radius: 20px;
        height: 30px;
        margin-top: 20px;
      }
    }
  }
}
</style>
