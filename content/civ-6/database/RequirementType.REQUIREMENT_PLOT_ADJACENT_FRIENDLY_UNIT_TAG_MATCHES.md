---
tags:
- RequirementType
title: REQUIREMENT_PLOT_ADJACENT_FRIENDLY_UNIT_TAG_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_ADJACENT_FRIENDLY_UNIT_TAG_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* Tag `String`
>	* IncludeCenter `Unknown`

## Samples

```SQL {title="REQUIRES_UNIT_IS_ADJACENT_RELIGIOUS_ALL_TAG"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_UNIT_IS_ADJACENT_RELIGIOUS_ALL_TAG",
		"REQUIREMENT_PLOT_ADJACENT_FRIENDLY_UNIT_TAG_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_UNIT_IS_ADJACENT_RELIGIOUS_ALL_TAG",
		"IncludeCenter",
		1
	),
	(
		"REQUIRES_UNIT_IS_ADJACENT_RELIGIOUS_ALL_TAG",
		"Tag",
		"CLASS_RELIGIOUS_ALL"
	);
	```

```SQL {title="ADJACENT_FRIENDLY_DRONE_UNIT_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"ADJACENT_FRIENDLY_DRONE_UNIT_REQUIREMENT",
		"REQUIREMENT_PLOT_ADJACENT_FRIENDLY_UNIT_TAG_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"ADJACENT_FRIENDLY_DRONE_UNIT_REQUIREMENT",
		"Tag",
		"CLASS_DRONE"
	);
	```
