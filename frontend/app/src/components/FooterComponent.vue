<template>
  <footer class="footer">
    <div class="footer__logo"><img src="../img/whiteLogo.png" alt="brand logo" /></div>
    <p class="footer__slogan">
      Our mission is to make conferences more exciting, easier managing questions and let introvers
      ask!
    </p>
    <div class="footer__socialMedia socialMedia">
      <p class="socialMedia__title">Check us on socialmedia</p>
      <div class="socialMedia__icons">
        <img src="../img/Discord.png" alt="" class="socialMedia__icon" />
        <img src="../img/Mail.png" alt="" class="socialMedia__icon" />
        <img src="../img/LinkedIn.png" alt="" class="socialMedia__icon" />
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'FooterComponent'
}
</script>

<style lang="scss">
.footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: $mainWhite;
  width: 100vw;
  height: 35vh;
  background-color: $darkBlue;
  padding: 80px;
  &__logo {
    width: 15%;
  }
  &__slogan {
    text-align: center;
    width: 15%;
  }
  &__socialMedia {
    width: 15%;
  }

  .socialMedia {
    &__title {
      font-size: 14px;
      margin-bottom: 20px;
      text-align: center;
    }
    &__icons {
      display: flex;
      justify-content: space-between;
    }
  }
}
</style>
