---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_X_FEATURE_TYPE
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_X_FEATURE_TYPE
>
> * Class: `CITIES`
> * Arguments:
>	* FeatureType `String`
>	* Amount `Integer`

## Samples

```SQL {title="CITY_HAS_1_OR_MORE_GEOTHERMALFISSURE_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"CITY_HAS_1_OR_MORE_GEOTHERMALFISSURE_REQUIREMENT",
		"REQUIREMENT_CITY_HAS_X_FEATURE_TYPE"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"CITY_HAS_1_OR_MORE_GEOTHERMALFISSURE_REQUIREMENT",
		"Amount",
		1
	),
	(
		"CITY_HAS_1_OR_MORE_GEOTHERMALFISSURE_REQUIREMENT",
		"FeatureType",
		"FEATURE_GEOTHERMAL_FISSURE"
	);
	```
