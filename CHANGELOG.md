# Changelog

## [5.5.2](https://github.com/imagekit-developer/imagekit-python/compare/v5.5.1...v5.5.2) (2026-05-25)


### Features

* initial stlc build ([8274740](https://github.com/imagekit-developer/imagekit-python/commit/8274740b92f67c625694f84b50ac3f044ec45a1f))


### Chores

* pin next release ([3e3f6b0](https://github.com/imagekit-developer/imagekit-python/commit/3e3f6b03e9c91b49e07794a928e90c879adb0782))
* trigger release-please ([0a0e2a2](https://github.com/imagekit-developer/imagekit-python/commit/0a0e2a235a4b3baa3e1202f0f9802dc3285e1eec))

## 5.5.1 (2026-05-17)

Full Changelog: [v5.5.0...v5.5.1](https://github.com/imagekit-developer/imagekit-python/compare/v5.5.0...v5.5.1)

### Chores

* trigger build ([ae54bfc](https://github.com/imagekit-developer/imagekit-python/commit/ae54bfcda1d717f8e23b90ba4f9f3407739458e3))
* trigger build for test ([ac69401](https://github.com/imagekit-developer/imagekit-python/commit/ac6940190c1896d465eb5c6b88e71ffdd0ec02d6))

## 5.5.0 (2026-05-13)

Full Changelog: [v5.4.0...v5.5.0](https://github.com/imagekit-developer/imagekit-python/compare/v5.4.0...v5.5.0)

### Features

* **api:** add no-enlarge crop modes and colorize transformation ([c4ddf30](https://github.com/imagekit-developer/imagekit-python/commit/c4ddf30c84d5d10a483ab5b2563510f049e414b2))
* **api:** manual updates ([965e263](https://github.com/imagekit-developer/imagekit-python/commit/965e26380c05a76c356fc994e0a92dc8efe3ac4e))
* **helper:** add colorize transformation to supported transforms ([8a96c55](https://github.com/imagekit-developer/imagekit-python/commit/8a96c55d03a9f1448954dd56510781b10b858436))
* **internal/types:** support eagerly validating pydantic iterators ([35bcec1](https://github.com/imagekit-developer/imagekit-python/commit/35bcec134edcbbf356f5f93d5a1e719f69b458a3))
* support setting headers via env ([39cbf90](https://github.com/imagekit-developer/imagekit-python/commit/39cbf90f16813f2ee8f477554ece14f804cc765d))
* **tests:** add colorize transformation to advanced URL generation test ([efa4d19](https://github.com/imagekit-developer/imagekit-python/commit/efa4d197ca7d8a3cba88243d8c187400f17b2dea))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([b3926a7](https://github.com/imagekit-developer/imagekit-python/commit/b3926a7b73d379cf56ce3985bc602254fda83f40))
* use correct field name format for multipart file arrays ([c89d2b3](https://github.com/imagekit-developer/imagekit-python/commit/c89d2b36f2049df445ac5f365ed8dac2544d116b))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([b22ab86](https://github.com/imagekit-developer/imagekit-python/commit/b22ab86e45de2bbc479942eaa27dd0c9b89cbc91))


### Chores

* configure new SDK language ([2b40f08](https://github.com/imagekit-developer/imagekit-python/commit/2b40f08e2757811dd14e29aed78f4f928fd97111))
* **internal:** more robust bootstrap script ([e5703df](https://github.com/imagekit-developer/imagekit-python/commit/e5703dfdb61f9842a508947555544ad9910a225d))
* **internal:** reformat pyproject.toml ([15a2ce1](https://github.com/imagekit-developer/imagekit-python/commit/15a2ce1f0293a0ab4d96792379e127f68f5cc64d))

## 5.4.0 (2026-04-13)

Full Changelog: [v5.3.0...v5.4.0](https://github.com/imagekit-developer/imagekit-python/compare/v5.3.0...v5.4.0)

### Features

* **api:** dam related webhook events ([8803680](https://github.com/imagekit-developer/imagekit-python/commit/8803680ae4bb3ea801d71520cc1354b7a1558bc6))
* **api:** fix spec indentation ([1a2417d](https://github.com/imagekit-developer/imagekit-python/commit/1a2417d4336d1b9403eb1bc2b65187209fe833c7))
* **api:** indentation fix ([6ad7341](https://github.com/imagekit-developer/imagekit-python/commit/6ad7341af30e43252519a3c44826be408323cbbe))
* **api:** merge with main to bring back missing parameters ([a07e952](https://github.com/imagekit-developer/imagekit-python/commit/a07e95275e50dcd975f3ec816420eee7645ce223))
* **api:** update webhook event names and remove DAM prefix ([bf9e082](https://github.com/imagekit-developer/imagekit-python/commit/bf9e082da50cea2f983b5bd88caca825e5039ec5))


### Bug Fixes

* **api:** extract shared schemas to prevent Go webhook union breaking changes ([9dcc234](https://github.com/imagekit-developer/imagekit-python/commit/9dcc234c1a5cd387a0989806819ced1b823277c0))
* **api:** rename DamFile events to File for consistency ([16b113f](https://github.com/imagekit-developer/imagekit-python/commit/16b113f1e6f42b4ac1af43c4cf0567cae55f6ecf))
* **client:** preserve hardcoded query params when merging with user params ([cbdc71f](https://github.com/imagekit-developer/imagekit-python/commit/cbdc71fee37ce26c0a05cabc55cb03b46c29b216))
* ensure file data are only sent as 1 parameter ([aa0272a](https://github.com/imagekit-developer/imagekit-python/commit/aa0272a8fe212b1a841031d25fddaa49359ec9d9))


### Documentation

* improve examples ([bc9d18e](https://github.com/imagekit-developer/imagekit-python/commit/bc9d18e102e37ad28dfe7181cbc3b8323ed79cb2))


### Refactors

* AITags to singular AITag schema with array items pattern ([96ad1bb](https://github.com/imagekit-developer/imagekit-python/commit/96ad1bb10dbfdad7112d82f5b6cc7199429e0fe3))

## 5.3.0 (2026-04-06)

Full Changelog: [v5.2.0...v5.3.0](https://github.com/imagekit-developer/imagekit-python/compare/v5.2.0...v5.3.0)

### Features

* **api:** dpr type update ([39d38db](https://github.com/imagekit-developer/imagekit-python/commit/39d38dbd0ca1e81dc84771e6a98a629f90e8dba9))
* **api:** Introduce lxc, lyc, lap parameters in overlays. ([5c9a08b](https://github.com/imagekit-developer/imagekit-python/commit/5c9a08b40db8734d022ff4670b8cf9204b2841fd))
* **api:** revert dpr breaking change ([7301276](https://github.com/imagekit-developer/imagekit-python/commit/73012764930ba8b461f98bbfd0349b395e46a7a4))
* **client:** import HelperResource and AsyncHelperResource in TYPE_CHECKING block ([22fc9cb](https://github.com/imagekit-developer/imagekit-python/commit/22fc9cb33d8c5724b0a042cc014ed6bdd54f7113))
* **internal:** implement indices array format for query and form serialization ([4533c28](https://github.com/imagekit-developer/imagekit-python/commit/4533c2831ad26cf5ef53da37c8d4fe095bb67bd8))
* **overlay:** support camelCase and snake_case for position properties in overlays ([5dd43b9](https://github.com/imagekit-developer/imagekit-python/commit/5dd43b9d84722fa62ffff4b8985282489003aa13))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([393174d](https://github.com/imagekit-developer/imagekit-python/commit/393174d253a106393b888aed50f9ca7623c9c06e))
* **pydantic:** do not pass `by_alias` unless set ([fda01e4](https://github.com/imagekit-developer/imagekit-python/commit/fda01e45e315c192d24a6183cd24fd43cbcb0722))
* sanitize endpoint path params ([fa1972c](https://github.com/imagekit-developer/imagekit-python/commit/fa1972cd605c2a7a81ad069161cc687d0ec4193d))


### Chores

* **ci:** skip lint on metadata-only changes ([5e9e6f3](https://github.com/imagekit-developer/imagekit-python/commit/5e9e6f35ba227e2fda57cb343f26f0ad0bcbb584))
* **ci:** skip uploading artifacts on stainless-internal branches ([15805f5](https://github.com/imagekit-developer/imagekit-python/commit/15805f5e6b642f0cebfbc8131f99f886e8e72e99))
* **dependencies:** require standardwebhooks 1.0.1 ([f7c4465](https://github.com/imagekit-developer/imagekit-python/commit/f7c44652ef95cfa1aefef380d280036158519007))
* format all `api.md` files ([09cbb17](https://github.com/imagekit-developer/imagekit-python/commit/09cbb17e722d374477b13fd4045201ab75ddcc7e))
* **internal:** add request options to SSE classes ([c0dee43](https://github.com/imagekit-developer/imagekit-python/commit/c0dee43afe3bc1f6ea35649532594e59fb4b8953))
* **internal:** bump dependencies ([6702b4b](https://github.com/imagekit-developer/imagekit-python/commit/6702b4bcd12af1d670a4b73a7d9bedd68ccc5560))
* **internal:** fix lint error on Python 3.14 ([89d503b](https://github.com/imagekit-developer/imagekit-python/commit/89d503b2a885f57edbbd6ffded3d1cddac61a53e))
* **internal:** make `test_proxy_environment_variables` more resilient ([821dd3f](https://github.com/imagekit-developer/imagekit-python/commit/821dd3f61db9b2be3297dc1b8a9e63d257df9ed1))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([487887e](https://github.com/imagekit-developer/imagekit-python/commit/487887eb0e4c405c0f8294e6a82ef6c7a2187c5c))
* **internal:** remove mock server code ([978ed61](https://github.com/imagekit-developer/imagekit-python/commit/978ed611a909e2d616b322e23bfe3d14e8f256f4))
* **internal:** tweak CI branches ([369ff73](https://github.com/imagekit-developer/imagekit-python/commit/369ff736880f83ac7196411241801fe9b04a7dfb))
* **internal:** update gitignore ([ab04623](https://github.com/imagekit-developer/imagekit-python/commit/ab04623fdceb9337d9519b119ead7949f1d4ed2f))
* **tests:** update webhook tests ([d94ada8](https://github.com/imagekit-developer/imagekit-python/commit/d94ada85d3c70d8f896fe276d73afd6c3fb17326))
* update mock server docs ([54f47c6](https://github.com/imagekit-developer/imagekit-python/commit/54f47c663b48f2b6a88bf05ba26a0f2a139ee752))
* update placeholder string ([d06cdca](https://github.com/imagekit-developer/imagekit-python/commit/d06cdca52df17c23df1d9cd8a468b8184bde219a))

## 5.2.0 (2026-02-02)

Full Changelog: [v5.1.2...v5.2.0](https://github.com/imagekit-developer/imagekit-python/compare/v5.1.2...v5.2.0)

### Features

* **api:** add customMetadata property to folder schema ([9b8597b](https://github.com/imagekit-developer/imagekit-python/commit/9b8597b8d8b4f11eb4c9e93ddbd924169fe9b0ea))
* **client:** add custom JSON encoder for extended type support ([2d7dd40](https://github.com/imagekit-developer/imagekit-python/commit/2d7dd4063992e7c49518ea8bca1bbf9dfec7aa9c))


### Bug Fixes

* **api:** add missing embeddedMetadata and video properties to FileDetails ([b1ffb23](https://github.com/imagekit-developer/imagekit-python/commit/b1ffb235b3f6dae292af80bd99d965db44db47f9))

## 5.1.2 (2026-01-29)

Full Changelog: [v5.1.1...v5.1.2](https://github.com/imagekit-developer/imagekit-python/compare/v5.1.1...v5.1.2)

### Bug Fixes

* **docs:** fix mcp installation instructions for remote servers ([df26dbd](https://github.com/imagekit-developer/imagekit-python/commit/df26dbdccce2814bbf30ee94853883a266211586))
* **tests:** update subtitle overlay references from "l-subtitle" to "l-subtitles" ([11fb58a](https://github.com/imagekit-developer/imagekit-python/commit/11fb58a82c0ff8eb5bdf4bf779b15ea85046604a))


### Chores

* **ci:** upgrade `actions/github-script` ([a75c01b](https://github.com/imagekit-developer/imagekit-python/commit/a75c01be5c51bdee1531f89b45519af872bb8c59))

## 5.1.1 (2026-01-20)

Full Changelog: [v5.1.0...v5.1.1](https://github.com/imagekit-developer/imagekit-python/compare/v5.1.0...v5.1.1)

### Bug Fixes

* vocab field is required ([4ab29b2](https://github.com/imagekit-developer/imagekit-python/commit/4ab29b248b89398b4334d6e1946a35a561997b2a))


### Chores

* **internal:** update `actions/checkout` version ([7826590](https://github.com/imagekit-developer/imagekit-python/commit/782659076636d78290d488da3f834343550627c8))

## 5.1.0 (2026-01-16)

Full Changelog: [v5.0.0...v5.1.0](https://github.com/imagekit-developer/imagekit-python/compare/v5.0.0...v5.1.0)

### Features

* add support for new transformations and layer modes in URL generation ([5fd87b1](https://github.com/imagekit-developer/imagekit-python/commit/5fd87b198090318eb19eb68c1d06ebc3636d735c))
* **api:** Add saved extensions API and enhance transformation options ([a0781ed](https://github.com/imagekit-developer/imagekit-python/commit/a0781edc19f2cbd78a87e973e0cc2277079fb02a))
* **client:** add support for binary request streaming ([f8580d6](https://github.com/imagekit-developer/imagekit-python/commit/f8580d644e31312e439a54704ca2e3858407ea0b))


### Bug Fixes

* add ai-tasks property to response schemas with enum values ([06de9eb](https://github.com/imagekit-developer/imagekit-python/commit/06de9ebc34e6fbf21f3863cd86d75556c429ff8f))
* **client:** loosen auth header validation ([40ef10e](https://github.com/imagekit-developer/imagekit-python/commit/40ef10e6e81ff3727a095aead127d296486a3c09))
* use async_to_httpx_files in patch method ([0014808](https://github.com/imagekit-developer/imagekit-python/commit/0014808307e55091a943d2f6b087fefbaee8ed0a))


### Chores

* **internal:** add `--fix` argument to lint script ([e6bf019](https://github.com/imagekit-developer/imagekit-python/commit/e6bf0196fe985302e11fb440cd3d215114a8e4c3))
* **internal:** add missing files argument to base client ([aec7892](https://github.com/imagekit-developer/imagekit-python/commit/aec7892b063c00b730afcdc440c0fa3ebe1cdae8))
* **internal:** codegen related update ([49635b4](https://github.com/imagekit-developer/imagekit-python/commit/49635b4dc6bd4268fc6a62f9df2a2e15c56afcee))
* speedup initial import ([ad1da84](https://github.com/imagekit-developer/imagekit-python/commit/ad1da84adad57d0a64a8f06a04c6ddb6b8f0e96b))


### Documentation

* prominently feature MCP server setup in root SDK readmes ([51c1a9a](https://github.com/imagekit-developer/imagekit-python/commit/51c1a9ae1545a25b574195ec73b83dab64d9becb))

## 5.0.0 (2025-12-13)

Full Changelog: [v0.0.1...v5.0.0](https://github.com/imagekit-developer/imagekit-python/compare/v0.0.1...v5.0.0)

### Features

* add bulk delete options ([c1c4d32](https://github.com/imagekit-developer/imagekit-python/commit/c1c4d3206b06594ba77a8a1c4dab7d0c5b74de9a))
* add file related functionalities ([681677b](https://github.com/imagekit-developer/imagekit-python/commit/681677bc60a207f433b4bc242c41e37f2d4c05a1))
* add sdk version to url ([9c3e67d](https://github.com/imagekit-developer/imagekit-python/commit/9c3e67d20f78b799e974889420ead23f457b5cfa))
* add url class for url genration ([5e615ed](https://github.com/imagekit-developer/imagekit-python/commit/5e615ed34386e3231c5c7963ff37ceb28ab7d2f1))
* **api:** python publish true ([8072dfd](https://github.com/imagekit-developer/imagekit-python/commit/8072dfd2eee562f98ac79fb5b11afe700e0dd6a3))
* implement client with all func. ([67dd4b2](https://github.com/imagekit-developer/imagekit-python/commit/67dd4b28822086009278e4ab3f85d52690e6e9b7))
* implement get_remote_url_metadata ([1272740](https://github.com/imagekit-developer/imagekit-python/commit/12727400dc5bc6678f6769c5143c11962f58eea4))
* **webhooks:** allow key parameter to accept bytes in unwrap method ([09ae375](https://github.com/imagekit-developer/imagekit-python/commit/09ae37575b6b1eba57f67c6b1dea3d59e10d270d))


### Bug Fixes

* binary file upload ([23c9c46](https://github.com/imagekit-developer/imagekit-python/commit/23c9c46f37a5b32144f86700227254e6f05bf491))
* change ubuntu latest to ubuntu-20.04 in test.yml ([1e4b551](https://github.com/imagekit-developer/imagekit-python/commit/1e4b55192d08ebf1aa436fa56832322477605942))
* Changes for CI/CD ([0bd2ac3](https://github.com/imagekit-developer/imagekit-python/commit/0bd2ac3e9b11e8269a2eacb2424d49ef58e37c5f))
* fix issue [#35](https://github.com/imagekit-developer/imagekit-python/issues/35),[#37](https://github.com/imagekit-developer/imagekit-python/issues/37),[#41](https://github.com/imagekit-developer/imagekit-python/issues/41),[#44](https://github.com/imagekit-developer/imagekit-python/issues/44) ([1f913c8](https://github.com/imagekit-developer/imagekit-python/commit/1f913c8e34a06afbffa93adbbc79e8a174a02dac))
* fix query params implementation ([2b7e6d4](https://github.com/imagekit-developer/imagekit-python/commit/2b7e6d4a148b6d94b52532846bd950d4eeeefac4))
* make ik-attachment option handle True boolean value ([6eb9cd0](https://github.com/imagekit-developer/imagekit-python/commit/6eb9cd099021a1fd9bcc9dfeb080ec610d4bcfbd))
* move the workflow to correct folder ([d9f933a](https://github.com/imagekit-developer/imagekit-python/commit/d9f933a8e78c61b8a61df1d74a28859f9e889378))
* request toolbelt to 0.10.1 in requirements/test/txt ([c22ed89](https://github.com/imagekit-developer/imagekit-python/commit/c22ed89208f69f7d8fb21cc777049d72dad40093))
* **serialization:** adjust custom_metadata type check for serialization ([6e3f209](https://github.com/imagekit-developer/imagekit-python/commit/6e3f2092cad4b2c3ed7d1f3086c7bfb2a9a51b08))


### Chores

* add func alias ([d7ce593](https://github.com/imagekit-developer/imagekit-python/commit/d7ce593318b24f33ba828b65042e16e892690b80))
* add init file ([0cbbd27](https://github.com/imagekit-developer/imagekit-python/commit/0cbbd27f00ac3fe36d3fbc0bf6fa2b015308576c))
* add publish github workflow script ([a275172](https://github.com/imagekit-developer/imagekit-python/commit/a275172c3e7096b7390665102bae4d95c718db9d))
* add required constants ([48de1c0](https://github.com/imagekit-developer/imagekit-python/commit/48de1c02295fb42d522f8ee930c16ee763d7b93d))
* add requirements files ([e8d3d9d](https://github.com/imagekit-developer/imagekit-python/commit/e8d3d9d60e946b036b3f8e37a9dbf1e68be5482d))
* add sample file for devs ([65d1a3f](https://github.com/imagekit-developer/imagekit-python/commit/65d1a3f77eaa5a5c9dba5202a75dee3c70aa64a0))
* add sample of get file metadata ([6d11584](https://github.com/imagekit-developer/imagekit-python/commit/6d115841c341df0f7a9d4d9bd0c33c1cf386d9c7))
* change pacakge name & fix import ([2c1734a](https://github.com/imagekit-developer/imagekit-python/commit/2c1734a6e12c935bc80f72ec6b8cdd5a971e5a47))
* fix package name ([c0c939d](https://github.com/imagekit-developer/imagekit-python/commit/c0c939d86fa5738855a0d6b606e33249ecd5a47a))
* fix package name ([4bc8041](https://github.com/imagekit-developer/imagekit-python/commit/4bc8041e22c6333710645ddc95446c9c348eea5b))
* fix sample ([2188038](https://github.com/imagekit-developer/imagekit-python/commit/2188038436aabfce68a3c1d7bb198ffda203dc72))
* init ([febccef](https://github.com/imagekit-developer/imagekit-python/commit/febccef19d6ca6ae2b6c4272d44ae1625c9f3391))
* remove unecessary workflow file ([97f19eb](https://github.com/imagekit-developer/imagekit-python/commit/97f19eb8284c5edfe164f98ad296ea1e69b21bf8))
* remove unused dummy methods from API documentation ([4727908](https://github.com/imagekit-developer/imagekit-python/commit/472790845ef7009aa3695fc084ef8c5d1d63f2ab))
* sync repo ([c6afd44](https://github.com/imagekit-developer/imagekit-python/commit/c6afd449e74ebb20ebc8d3390355219fccaf2178))
* unused import removed ([22774ff](https://github.com/imagekit-developer/imagekit-python/commit/22774fff1ac08c0573efc06ab10f3fe31e6d3f69))
* update SDK settings ([81f0de9](https://github.com/imagekit-developer/imagekit-python/commit/81f0de954a0d531c6b98354386462f4186a58aba))


### Build System

* add url and requirements ([211228e](https://github.com/imagekit-developer/imagekit-python/commit/211228ef91fe29b83507c89f3bf22cfb6b1c8184))
* add url and requirements ([683ad01](https://github.com/imagekit-developer/imagekit-python/commit/683ad016099d4e4614b6f369bff69d9a7422029e))
* add url and requirements ([#2](https://github.com/imagekit-developer/imagekit-python/issues/2)) ([211228e](https://github.com/imagekit-developer/imagekit-python/commit/211228ef91fe29b83507c89f3bf22cfb6b1c8184))
