---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_FEATURE
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_FEATURE
>
> * Class: `CITIES`
> * Arguments:
>	* FeatureType `String`

## Samples

```SQL {title="REQUIRES_PAITITI_IN_CITY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PAITITI_IN_CITY",
		"REQUIREMENT_CITY_HAS_FEATURE"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PAITITI_IN_CITY",
		"FeatureType",
		"FEATURE_PAITITI"
	);
	
```
