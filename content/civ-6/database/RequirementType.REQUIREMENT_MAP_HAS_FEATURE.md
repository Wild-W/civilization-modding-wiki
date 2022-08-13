---
tags:
- RequirementType
title: REQUIREMENT_MAP_HAS_FEATURE
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_MAP_HAS_FEATURE
>
> * Class: `ANY`
> * Arguments:
>	* FeatureType `String`
>		* [Features.FeatureType]

## Samples

```SQL {title="MAP_CONTAINS_BERMUDA_TRIANGLE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"MAP_CONTAINS_BERMUDA_TRIANGLE",
		"REQUIREMENT_MAP_HAS_FEATURE"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"MAP_CONTAINS_BERMUDA_TRIANGLE",
		"FeatureType",
		"FEATURE_BERMUDA_TRIANGLE"
	);
	```
