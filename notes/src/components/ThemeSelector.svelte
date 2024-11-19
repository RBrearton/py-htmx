<script lang="ts">
  import { onMount } from "svelte";

  export let lightThemeName: string;
  export let darkThemeName: string;

  // Default to light theme.
  let isDarkTheme = false;

  // Function to toggle the theme and save it to localStorage.
  function toggleTheme() {
    // Get the theme name.
    const theme = isDarkTheme ? darkThemeName : lightThemeName;

    // Set the theme on the document element and save it to localStorage.
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
  }

  // On component mount, check localStorage for the saved theme and apply it.
  onMount(() => {
    const savedTheme = localStorage.getItem("theme") || lightThemeName;
    document.documentElement.setAttribute("data-theme", savedTheme);
    isDarkTheme = savedTheme === darkThemeName;
  });
</script>

<label class="flex flex-row cursor-pointer gap-2 px-5">
  <!-- Add a sun icon for the light mode. -->
  <i class="material-icons text-primary-content">sunny</i>

  <!-- Add a checkbox input to control the theme. -->
  <input
    type="checkbox"
    class="toggle theme-controller"
    bind:checked={isDarkTheme}
    on:change={toggleTheme}
  />

  <!-- Add a moon icon for the dark mode. -->
  <i class="material-icons text-primary-content">dark_mode</i>
</label>
