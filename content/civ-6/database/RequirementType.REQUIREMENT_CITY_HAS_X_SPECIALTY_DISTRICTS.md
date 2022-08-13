---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_X_SPECIALTY_DISTRICTS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_X_SPECIALTY_DISTRICTS
>
> * Class: `CITIES`
> * Arguments:
>	* MustBeFunctioning `Boolean`
>	* Amount `Integer`
>		* The provided amount.

## Samples

```SQL {title="REQUIRES_CITY_HAS_0_SPECIALTY_DISTRICTS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_CITY_HAS_0_SPECIALTY_DISTRICTS",
		"REQUIREMENT_CITY_HAS_X_SPECIALTY_DISTRICTS",
		1
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_CITY_HAS_0_SPECIALTY_DISTRICTS",
		"Amount",
		1
	),
	(
		"REQUIRES_CITY_HAS_0_SPECIALTY_DISTRICTS",
		"MustBeFunctioning",
		0
	);
	
```
