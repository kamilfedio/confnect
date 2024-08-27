<template>
  <div v-if="showScrollArrow" class="arrow" @click="scrollToTop">
    <img src="../../img/icons/arrowUp.png" alt="arrow icon" class="arrow__icon" />
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
          <img src="../../img/icons/arrow.png" alt="arrow" class="introduction__iconImg" />
        </div>
        <div class="introduction__icon">
          <img src="../../img/icons/arrow.png" alt="arrow" class="introduction__iconImg" />
        </div>
        <div class="introduction__icon">
          <img src="../../img/icons/arrow.png" alt="arrow" class="introduction__iconImg" />
        </div>
      </div>
      <div class="introduction__logo">
        <img src="../../img/transparentBgc_logo.png" alt="brand logo" class="introduction__img" />
      </div>
      <p class="introduction__text">Your assistant in presentations</p>
      <button class="introduction__btn">Get started</button>
    </section>
    <section class="checkUs">
      <div class="checkUs__title">
        <img src="../../img/line.png" alt="line" class="checkUs__img" />
        <p @click="scrollToFeatures">Check us below!</p>
        <img src="../../img/line.png" alt="line" class="checkUs__img" />
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

<script src="./LandingPage.vue.ts"></script>
<style src="./LandingPage.scss" scoped></style>
