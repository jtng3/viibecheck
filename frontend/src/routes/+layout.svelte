<script lang="ts">
	import '../app.postcss';
	import { onMount } from 'svelte';
	import Logo from '$lib/components/Logo.svelte';

	function success(position: any) {
		console.log(position.coords.latitude, position.coords.longitude);
		const latitude = position.coords.latitude;
		const longitude = position.coords.longitude;
	}

	function error() {
		alert('Sorry, no position available.');
	}

	const options = {
		enableHighAccuracy: true,
		maximumAge: 30000,
		timeout: 27000
	};

	onMount(() => {
		if ('geolocation' in navigator) {
			const watchID = navigator.geolocation.watchPosition(success, error, options);
		} else {
			alert('Geolocation is not supported in this browser.');
		}
	});
</script>

<div class="grid grid-cols-1 min-w-screen min-h-screen bg-primary-100 items-start">
	<div class="relative w-full flex flex-col justify-self-center justify-center">
		<div
			class="fixed top-0 bg-primary-700 h-[80px] w-full px-10 flex flex-row items-center justify-center gap-10 text-white"
		>
			<a class="hover:text-white/50" href="/"
				><div class="font-bold text-xl tracking-widest">ViibeCheck™</div>
			</a>
			<a class="hover:text-white/50" href="/">Home</a>
			<a class="hover:text-white/50" href="/about">About</a>
			<a class="hover:text-white/50" href="/search">Search</a>
			<a class="hover:text-white/50" href="/new_report">New Report</a>
			<a class="hover:text-white/50" href="/resources">Resources</a>
		</div>
		<div class="pt-20">
			<div class="flex items-center justify-center py-5">
				<Logo />
			</div>
			<main class="flex w-full p-10 justify-center pt-0">
				<!-- Border is only for temporary vision of how we move items within the page -->
				<div class="grid grid-cols-1 w-full max-w-6xl border rounded-xl bg-white p-10">
					<slot />
				</div>
			</main>
		</div>
	</div>
	<div class="pt-20" />
	<footer
		class="fixed bottom-0 w-full h-[100px] border-t-4 border-primary-400 px-10 pt-5 text-gray-600 bg-white"
	>
		Built by JT and LP © 2023, All rights reserved.
	</footer>
</div>
