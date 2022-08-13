---
tags:
- RequirementType
title: REQUIREMENT_CITY_LOCATION_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_LOCATION_MATCHES
>
> * Class: `CITIES`
> * Arguments:
>	* Y `Integer`
>	* X `Integer`

## Samples

```SQL {title="WARMACHINE_CITY_IS_PARIS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"WARMACHINE_CITY_IS_PARIS",
		"REQUIREMENT_CITY_LOCATION_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"WARMACHINE_CITY_IS_PARIS",
		"X",
		9
	),
	(
		"WARMACHINE_CITY_IS_PARIS",
		"Y",
		14
	);
	
```
