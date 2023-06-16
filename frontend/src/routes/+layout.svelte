<script lang="ts">
	import '../app.postcss';
	//START: Geolocation api to be later provided to search component to look for reports within a 50 mile radius
	function success(position: any) {
		console.log(position.coords.latitude, position.coords.longitude);
	}
	function error() {
		alert('Sorry, no position available.');
	}
	const options = {
		enableHighAccuracy: true,
		maximumAge: 30000,
		timeout: 27000
	};
	let navigator: any;
	const watchID: any = navigator.geolocation.watchPosition(success, error, options);
	//End: Geolocation api data
</script>

<div class="grid grid-cols-1 min-w-screen min-h-screen bg-primary-100 items-start">
	<div class="relative w-full flex flex-col justify-self-center justify-center">
		<div
			class="static bg-primary-700 h-[80px] w-full px-10 flex flex-row items-center justify-center gap-10 text-white"
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
		<main class="flex w-full p-10 justify-center">
			<!-- Border is only for temporary vision of how we move items within the page -->
			<div class="grid grid-cols-1 w-full max-w-6xl border bg-white p-10">
				<slot />
			</div>
		</main>
	</div>
	<footer
		class="fixed bottom-0 w-full h-[100px] border-t-4 border-primary-400 px-10 pt-5 text-gray-600 bg-white"
	>
		Built by JT and LP © 2023, All rights reserved.
	</footer>
</div>
