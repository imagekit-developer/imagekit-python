# Changelog

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
