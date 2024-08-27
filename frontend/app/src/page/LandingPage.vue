<template>
  <div v-if="showScrollArrow" class="arrow" @click="scrollToTop">
    <img src="../img/icons/arrowUp.png" alt="arrow icon" class="arrow__icon" />
  </div>
  <header>
    <div class="header">
      <div class="header__brand">Confnect</div>
      <div class="header__nav">
        <LandingPageNavigation
          :onScrollToFeatures="scrollToFeatures"
          :onScrollToAbout="scrollToAbout"
          :onScrollToContact="scrollToContact"
        />
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
      <div class="introduction__icons">
        <div class="introduction__icon">
          <img src="../img/icons/arrow.png" alt="arrow" class="introduction__iconImg" />
        </div>
        <div class="introduction__icon">
          <img src="../img/icons/arrow.png" alt="arrow" class="introduction__iconImg" />
        </div>
        <div class="introduction__icon">
          <img src="../img/icons/arrow.png" alt="arrow" class="introduction__iconImg" />
        </div>
      </div>
      <div class="introduction__logo">
        <img src="../img/transparentBgc_logo.png" alt="brand logo" class="introduction__img" />
      </div>
      <p class="introduction__text">Your assistant in presentations</p>
      <button class="introduction__btn">Get started</button>
    </section>
    <section class="checkUs">
      <div class="checkUs__title">
        <img src="../img/line.png" alt="line" class="checkUs__img" />
        <p @click="scrollToFeatures">Check us below!</p>
        <img src="../img/line.png" alt="line" class="checkUs__img" />
      </div>
      <div class="checkUs__screens screens">
        <div class="screens__item">
          <div class="screens__imgContainer">
            <div class="screens__img screen1"></div>
          </div>
        </div>
        <div class="screens__item">
          <div class="screens__imgContainer">
            <div class="screens__img screen2"></div>
          </div>
        </div>
        <div class="screens__item">
          <div class="screens__imgContainer">
            <div class="screens__img screen3"></div>
          </div>
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
        <div class="feature__container">
          <div class="feature__imgContainer">
            <div class="feature__img">
              <div class="feature__imgContent feature1"></div>
            </div>
          </div>
          <p>Live questions</p>
        </div>
        <div class="feature__container">
          <div class="feature__imgContainer">
            <div class="feature__img">
              <div class="feature__imgContent feature2"></div>
            </div>
          </div>
          <p>Feedback</p>
        </div>
        <div class="feature__container">
          <div class="feature__imgContainer">
            <div class="feature__img">
              <div class="feature__imgContent feature3"></div>
            </div>
          </div>
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
        <div class="contactForm__areaContainer">
          <textarea
            v-model="userMessage"
            class="contactForm__textArea"
            placeholder="Your issue..."
          ></textarea>
          <p v-if="messageError" class="contactForm__error">{{ messageError }}</p>
        </div>
        <div class="contactForm__details">
          <h1 class="contactForm__title">Contact Form</h1>
          <input
            v-model="userEmail"
            type="text"
            class="contactForm__input"
            placeholder="Your email..."
          />
          <p v-if="emailError" class="contactForm__error">{{ emailError }}</p>
          <input
            v-model="userName"
            type="text"
            class="contactForm__input"
            placeholder="Your name..."
          />
          <p v-if="nameError" class="contactForm__error">{{ nameError }}</p>
          <button @click="sendMessage" class="contactForm__btn">Send</button>
        </div>
      </div>
    </section>
  </main>
</template>

<script lang="ts">
import LandingPageNavigation from '../components/LandingPageNavigation.vue'
export default {
  name: 'LandingPage',
  components: {
    LandingPageNavigation
  },
  data() {
    return {
      userMessage: '',
      userName: '',
      userEmail: '',
      showScrollArrow: false,
      messageError: '',
      emailError: '',
      nameError: ''
    }
  },
  methods: {
    scrollToFeatures() {
      const section = document.querySelector('.feature')
      if (section) {
        section.scrollIntoView({ behavior: 'smooth' })
      }
    },
    scrollToAbout() {
      const section = document.querySelector('.journay')
      if (section) {
        section.scrollIntoView({ behavior: 'smooth' })
      }
    },
    scrollToContact() {
      const section = document.querySelector('.writeToUs')
      if (section) {
        section.scrollIntoView({ behavior: 'smooth' })
      }
    },
    scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' })
    },
    handleScroll() {
      this.showScrollArrow = window.scrollY > window.innerHeight
    },
    validateEmail() {
      const atIndex = this.userEmail.indexOf('@')
      const dotAfterAt = this.userEmail.indexOf('.', atIndex)

      if (atIndex === -1 || dotAfterAt === -1) {
        this.emailError = 'Incorrect email format'
      } else return
    },
    validateMessage() {
      if (this.userMessage.length < 10) {
        this.messageError = 'The message must contain at least 10 characters'
      } else return
    },
    validateName() {
      if (this.userName.length < 3) {
        this.nameError = 'The name must contain at least 3 characters'
      } else return
    },
    async sendMessage() {
      this.messageError = ''
      this.emailError = ''
      this.nameError = ''
      const url = 'http://0.0.0.0:8000/forms/'
      this.validateEmail()
      this.validateMessage()
      this.validateName()
      if (this.messageError || this.emailError || this.nameError) {
        return
      } else {
        fetch(url, {
          method: 'POST',
          headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            email: this.userEmail,
            name: this.userName,
            content: this.userMessage
          })
        })
          .then((response) => response.json())
          .then((data) => console.log(data))
          .catch((error) => console.error('Error:', error))
        this.userMessage = ''
        this.userName = ''
        this.userEmail = ''
      }
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll)
    this.handleScroll()
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll)
  }
}
</script>

<style scoped lang="scss">
.arrow {
  width: 50px;
  height: 50px;
  border-radius: 17px;
  background-color: $mainGreen;
  position: fixed;
  right: 50px;
  bottom: 50px;
  cursor: pointer;
  &__icon {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
}

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
    transition: 0.3s;
    cursor: pointer;
    &:hover {
      color: $mainWhite;
      background-color: $mainDarkBlue;
    }
  }
  @media (max-width: 430px) {
    &__brand {
      padding-right: 5px;
    }
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
    &__icons {
      margin: 60px auto 0 auto;
      position: relative;
      width: 100%;
    }
    &__icon {
      position: absolute;
      top: 0;
      left: 50%;
      transform: translateY(-50%);
      animation: arrowAnimation 1.5s linear infinite;
      &:nth-child(2) {
        top: 10px;
        animation-delay: 0.3s;
      }
      &:nth-child(3) {
        top: 20px;
        animation-delay: 0.6s;
      }
    }
    &__logo {
      width: 100%;
      margin: 0 auto;
      margin-top: 80px;
      img {
        width: 100%;
      }
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
      transition: 0.3s;
      cursor: pointer;
      &:hover {
        color: $mainWhite;
        background-color: $mainDarkBlue;
      }
    }
    @media (max-width: 430px) {
      width: 80%;
      &__slogan {
        margin-top: 40px;
      }
      &__logo {
        transform: scale(0.7);
        width: 100%;
        margin-top: 40px;
      }
      &__btn {
        margin-top: 40px;
      }
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
        cursor: pointer;
      }
    }
    &__screens {
      margin-top: 40px;
    }
    &__text {
      margin-top: 30px;
      font-size: 1.2em;
      padding: 10px;
      text-align: center;
      color: $mainDarkBlue;
    }

    .screens {
      padding: 40px;
      padding-bottom: 0;
      display: flex;
      justify-content: space-between;
      &__item {
        width: 200px;
        height: 266px;
        border-radius: 40px;
        transform: rotate(-40deg);
        background-color: $lightGrey;
      }
      &__imgContainer {
        width: 100%;
        height: 250px;
        border-radius: 40px;
        transform: translate(-12px, 12px);
        overflow: hidden;
      }
      &__img {
        background-size: contain;
        background-repeat: no-repeat;
        width: 271px;
        height: 344px;
        transform: rotate(40deg);
        position: absolute;
        transition: 0.5s;
        &.screen1 {
          background-image: url('../img/screen1.png');
          top: -17%;
          left: -29%;
        }
        &.screen2 {
          background-image: url('../img/screen2.png');
          top: -10%;
          left: -21%;
        }
        &.screen3 {
          background-image: url('../img/screen3.png');
          top: -13%;
          left: -31%;
        }
        &:hover {
          transform: rotate(40deg) scale(1.2);
        }
      }
    }
    @media (max-width: 1230px) {
      .screens {
        width: 90%;
        margin: 0 auto;
        transform: scale(0.9);
      }
    }

    @media (max-width: 960px) {
      .screens {
        flex-wrap: wrap;
        overflow: hidden;
        justify-content: space-around;
        &__item {
          margin: 0 6%;
        }
      }
    }
    @media (max-width: 430px) {
      margin-top: 80px;
      &__text {
        margin-top: 0;
      }
      .screens {
        padding-top: 0;
        &__item {
          margin-top: 10px;
          transform: rotate(-45deg) scale(0.8);
        }
      }
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
      text-align: center;
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
    @media (max-width: 430px) {
      margin-top: 80px;
    }
  }
  .feature {
    &__images {
      display: flex;
      justify-content: space-between;
      margin-top: 80px;
      width: 65%;
      font-size: 1.6em;
      color: $mainDarkBlue;
      text-align: center;
    }
    &__container p {
      padding: 10px 0;
    }
    &__imgContainer {
      width: 205px;
      height: 205px;
      background-color: $mainGreen;
      border-radius: 40px;
      position: relative;
    }
    &__img {
      width: 200px;
      height: 200px;
      background-size: contain;
      background-repeat: no-repeat;
      border-radius: 40px;
      position: absolute;
      top: 5px;
      bottom: 0;
      overflow: hidden;
    }
    &__imgContent {
      background-size: contain;
      background-repeat: no-repeat;
      width: 100%;
      height: 100%;
      transition: 0.5s;
      &.feature1 {
        background-image: url('../img/features1.png');
      }
      &.feature2 {
        background-image: url('../img/features2.png');
      }
      &.feature3 {
        background-image: url('../img/features3.png');
      }
      &:hover {
        transform: scale(1.4);
        background-position: 25px 25px;
      }
    }
    @media (max-width: 960px) {
      &__images {
        flex-wrap: wrap;
        justify-content: space-around;
      }
      &__container {
        width: 50%;
      }
      &__imgContainer {
        margin: 0 auto;
      }
    }
    @media (max-width: 430px) {
      margin-top: 80px;
      &__images {
        width: 90%;
      }
      &__container {
        width: 100%;
      }
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
        transition: 0.3s;
        cursor: pointer;
        &:hover {
          color: $mainWhite;
          background-color: $mainDarkBlue;
        }
      }
      &__error {
        color: $errorRed;
        font-weight: bold;
        font-size: 1.4em;
      }
    }
    @media (max-width: 430px) {
      .contactForm {
        width: 90%;
        &__textArea {
          width: 50%;
        }
        &__details {
          width: 50%;
        }
      }
    }
  }
}

@keyframes arrowAnimation {
  0% {
    opacity: 0;
  }
  20% {
    opacity: 1;
  }
  40% {
    opacity: 1;
  }
  60% {
    opacity: 0;
  }
  100% {
    opacity: 0;
  }
}
</style>
