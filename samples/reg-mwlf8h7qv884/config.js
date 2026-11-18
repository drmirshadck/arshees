/* Neuron Homoeos — TEST of DotCom's own calendar (no Cal.com). Settings for booking.js, doctor.html and manage.html. */
window.SITE = {
  doctor: { name: "Neuron Homoeos", photo: "doctor1.jpg", role: "Online Homoeopathy Clinic · Kozhikode" },
  theme: { brand: "#005293", brandDeep: "#04244d", accent: "#0068bb", light: "#a6cbe1" },
  helper: { url: "https://dotcom-by-arshees-calendar-test.drmirshadck.workers.dev" },
  doctors: [
    { id: "nagaraja", name: "Dr Nagaraja Rao", photo: "doctor1.jpg", title: "BHMS MD · Pediatrician" },
    { id: "imran", name: "Dr Imran Khan", photo: "doctor2.jpg", title: "BHMS MD · General" }
  ],
  consultations: { types: [
    { calSlug: "online-video-consultation", name: "Online video consultation", duration: "20 minutes", fee: 1200 }
  ] },
  payment: { upiId: "test@upi", payeeName: "Neuron Homoeos (TEST)" },
  cal: { username: "" },
  video: { roomUrl: "" },
  contact: { whatsapp: "971586576586", clinicName: "Neuron Homoeos", phoneDisplay: "0586576586" }
};
