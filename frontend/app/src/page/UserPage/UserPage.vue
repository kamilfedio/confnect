<template>
  <div class="wrapper">
    <header>
      <div class="topPanel">
        <img src="../../img/transparentBgc_logo.png" alt="brandLogo" class="topPanel__logo" />
        <div class="topPanel__profile profile">
          <div class="profile__name">
            <p class="profile__firstName">Jan</p>
            <p class="profile__surName">Krupa</p>
          </div>
          <div class="profile__img"></div>
        </div>
      </div>
      <p class="welcome">Nice to see you Jan</p>
    </header>
    <main>
      <div class="section">
        <h1 class="section__title">When will we meet somebody?</h1>
        <div class="section__blocks">
          <div class="section__block">play</div>
          <div class="section__block">ask</div>
          <div class="section__block">event</div>
        </div>
        <p class="section__text">
          List of your all events and calendar with marked events. If you to add new event click
          green box!
        </p>
      </div>
      <div class="mainSection">
        <div class="mainSection__events">
          <div class="addEvent">
            <p class="addEvent__txt">+ Add Event</p>
          </div>
          <EventComponent />
          <EventComponent />
        </div>
        <div class="mainSection__other">
          <SearchPanel />
        </div>
      </div>
    </main>
  </div>
</template>

<script src="./UserPage.vue.ts"></script>
<style src="./UserPage.scss" scoped></style>
