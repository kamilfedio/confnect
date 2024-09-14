<template>
  <div class="bgc">
    <div>addEvent</div>
    <form @submit.prevent="submitForm">
      <input type="text" v-model="name" />
      <input type="text" v-model="description" />
      <input type="text" v-model="place" />
      <input type="date" v-model="date" />
      <input type="text" v-model="optional_info" />
      <button type="submit">SUBMIT</button>
    </form>
  </div>
</template>

<script src="./AddEvent.vue.ts"></script>
<style src="./AddEvent.scss" scoped></style>
