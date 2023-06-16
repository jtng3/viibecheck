<script lang="ts">
	import Fuse from 'fuse.js';

	let showSearch = false;
	let searchPattern: any;
	let fuse: any;
	let reports: any[] = [];

	let searchableReports = [
		{ title: 'Weirdo in PDX', name: 'Jack the Ripper', report_date: '2023-01-01' },
		{ title: 'Tinder Horror Story', name: 'Jeffrey Dahmer', report_date: '2022-01-01' },
		{ title: 'Bad Hike', name: 'Harold Shipman', report_date: '2021-01-01' },
		{ title: 'Creepy Creeper', name: 'John Wayne Gacy', report_date: '2020-01-01' },
		{ title: 'Almost R*ped', name: 'H.H. Holmes', report_date: '2019-01-01' },
		{ title: 'Pedophile!!!', name: 'Pedro Lopez', report_date: '2018-01-01' },
		{ title: 'Is TOO into guns', name: 'Ted Bundy', report_date: '2017-01-01' }
	];

	const searchOptions = {
		includeScore: true,
		threshold: 0.5, // value 0 is very strict, value 1 is not strict, .6 is the default,
		keys: ['title', 'name', 'report_date']
	};

	function search(reports: any) {
		fuse = new Fuse(reports, searchOptions);
	}

	$: searchPattern && searchReports();

	const searchReports = () => {
		showSearch = true;
		search(searchableReports);
		if (fuse) {
			if (searchPattern) {
				const searchResult = fuse.search(searchPattern);
				const filteredTodos = searchResult.map((obj: any) => obj.item);
				reports = filteredTodos;
			} else {
				reports = [];
			}
		}
	};
</script>

<svelte:head>
	<title>viibecheck</title>
	<meta name="Search" content="Search Page" />
</svelte:head>

<!-- Option A -->
<div class="pb-20">
	<div class="text-primary-600 text-xl font-bold pb-5">Search ViibeCheck™</div>
	<form class="grid grid-cols-1 gap-5">
		<div class="flex flex-row w-full gap-10">
			<input
				class="rounded-md focus:border-primary-400 focus:ring-0 border text-gray-500 border-primary-600 w-full placeholder:text-primary-400"
				placeholder="First Name"
				type="text"
			/>
			<input
				class="rounded-md focus:border-primary-400 focus:ring-0 border text-gray-500 border-primary-600 w-full placeholder:text-primary-400"
				placeholder="Last Name"
				type="text"
			/>
		</div>
		<input
			placeholder="Phone Number"
			class="rounded-md focus:border-primary-400 focus:ring-0 border text-gray-500 border-primary-600 w-full placeholder:text-primary-400"
			type="text"
		/>
	</form>
</div>
<!-- Option B -->
<div class="grid grid-cols-1 gap-4">
	<div class="text-primary-600 text-xl font-bold">Search through previous reports</div>
	<div
		class="flex flex-row items-center pl-5 rounded-xl border-2 border-primary-500 overflow-hidden"
	>
		<div
			class="text-lg hover:text-primary-600/50 font-semibold tracking-tight text-primary-600 pr-4"
		>
			Search
		</div>
		<input
			bind:value={searchPattern}
			on:input={searchReports}
			class="focus:border-primary-400 focus:ring-0 border-0 text-gray-500 border-l-2 border-primary-400 w-full placeholder:text-primary-400"
			type="text"
			placeholder="Name of the person who gave you ick vibes"
			name=""
			id=""
		/>
	</div>
	{#if showSearch}
		<div>
			<div class="text-primary-600 text-xl font-bold">Results</div>
			<div class="p-4 border rounded-md overflow-hidden">
				<!-- Consider using a table, maybe we want another way to display data? refer to Jaegers input -->

				{#each reports as report}
					{@const title = report.title}
					{@const name = report.name}
					{@const reportDate = report.report_date}
					<div class="flex flex-row gap-4">
						<div class="font-bold underline text-primary-600 whitespace-nowrap">{title}:</div>
						<div class="font-semibold text-primary-500 whitespace-nowrap">{name}</div>
						<div class="font-semibold text-primary-400 w-full text-end whitespace-nowrap">
							{reportDate}
						</div>
					</div>
				{/each}
			</div>
		</div>
	{/if}
</div>
