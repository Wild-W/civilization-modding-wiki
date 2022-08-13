---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_COMPLETED_PROJECT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_COMPLETED_PROJECT
>
> * Class: `PLAYERS`
> * Arguments:
>	* ProjectType `String`
>		* [Projects.ProjectType]
>	* MinimumCompletions `Integer`

## Samples

```SQL {title="REQUIRES_PLAYER_COMPLETED_EXOPLANET_EXPEDITION"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_COMPLETED_EXOPLANET_EXPEDITION",
		"REQUIREMENT_PLAYER_HAS_COMPLETED_PROJECT"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_COMPLETED_EXOPLANET_EXPEDITION",
		"MinimumCompletions",
		1
	),
	(
		"REQUIRES_PLAYER_COMPLETED_EXOPLANET_EXPEDITION",
		"ProjectType",
		"PROJECT_LAUNCH_EXOPLANET_EXPEDITION"
	);
	
```
