<template>
  <form @submit.prevent="handleSubmit">
    <input type="file" @change="handleFileChange" />
    <button type="submit">Upload</button>

    <div v-if="detections.length">
      <h3>Detections:</h3>
      <ul>
        <li v-for="(d, i) in detections" :key="i">
          {{ d.name }} at [{{ d.xmin }}, {{ d.ymin }}]
        </li>
      </ul>
    </div>

    <div v-if="errorMessage" style="color: red;">
      <p>Error: {{ errorMessage }}</p>
    </div>
  </form>
</template>

<script setup>
import { ref } from 'vue'

const imageFile = ref(null)
const detections = ref([])
const errorMessage = ref('')

const handleFileChange = (e) => {
  imageFile.value = e.target.files[0]
  errorMessage.value = ''
}

const handleSubmit = async () => {
  detections.value = []
  errorMessage.value = ''

  const formData = new FormData()
  formData.append('image', imageFile.value)

  try {
    const res = await fetch(`/detect`, {
      method: 'POST',
      body: formData
    })

    const text = await res.text()
    console.log('Raw backend response:', text)

    if (!res.ok) {
      errorMessage.value = `HTTP ${res.status}: ${text}`
      return
    }

    const data = JSON.parse(text)
    detections.value = data.detections || []
  } catch (err) {
    errorMessage.value = 'Failed to fetch or parse response'
    console.error('Error:', err)
  }
}
</script>
