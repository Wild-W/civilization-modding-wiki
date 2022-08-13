---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_GOVERNOR_WITH_X_TITLES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_GOVERNOR_WITH_X_TITLES
>
> * Class: `CITIES`
> * Arguments:
>	* Established `Boolean`
>	* Amount `Integer`

## Samples

```SQL {title="REQUIRES_CITY_HAS_2_TITLE_GOVERNOR"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CITY_HAS_2_TITLE_GOVERNOR",
		"REQUIREMENT_CITY_HAS_GOVERNOR_WITH_X_TITLES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_CITY_HAS_2_TITLE_GOVERNOR",
		"Amount",
		2
	),
	(
		"REQUIRES_CITY_HAS_2_TITLE_GOVERNOR",
		"Established",
		1
	);
	```
