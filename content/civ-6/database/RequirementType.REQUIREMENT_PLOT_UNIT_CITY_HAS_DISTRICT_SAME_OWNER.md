---
tags:
- RequirementType
title: REQUIREMENT_PLOT_UNIT_CITY_HAS_DISTRICT_SAME_OWNER
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_UNIT_CITY_HAS_DISTRICT_SAME_OWNER
>
> * Class: `PLOTS`
> * Arguments:
>	* DistrictType `String`

## Samples

```SQL {title="REQUIRES_PLOT_UNIT_CITY_HAS_COTHON_SAME_OWNER"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLOT_UNIT_CITY_HAS_COTHON_SAME_OWNER",
		"REQUIREMENT_PLOT_UNIT_CITY_HAS_DISTRICT_SAME_OWNER"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLOT_UNIT_CITY_HAS_COTHON_SAME_OWNER",
		"DistrictType",
		"DISTRICT_COTHON"
	);
	```
