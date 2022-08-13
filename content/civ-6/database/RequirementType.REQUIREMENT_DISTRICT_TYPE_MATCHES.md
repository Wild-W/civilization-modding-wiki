---
tags:
- RequirementType
title: REQUIREMENT_DISTRICT_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_DISTRICT_TYPE_MATCHES
>
> * Class: `DISTRICTS`
> * Arguments:
>	* DistrictType `String`
>		* [Districts.DistrictType]

## Samples

```SQL {title="OPPONENT_PLOT_IS_CITY_CENTER_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"OPPONENT_PLOT_IS_CITY_CENTER_REQUIREMENT",
		"REQUIREMENT_DISTRICT_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"OPPONENT_PLOT_IS_CITY_CENTER_REQUIREMENT",
		"DistrictType",
		"DISTRICT_CITY_CENTER"
	);
	
```
