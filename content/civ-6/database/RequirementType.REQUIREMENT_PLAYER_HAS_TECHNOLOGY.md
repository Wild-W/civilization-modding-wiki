---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_TECHNOLOGY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_TECHNOLOGY
>
> * Class: `PLAYERS`
> * Arguments:
>	* TechnologyType `String`
>		* [Technologies.TechnologyType]

## Samples

```SQL {title="REQUIRES_PLAYER_HAS_APPRENTICESHIP"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_APPRENTICESHIP",
		"REQUIREMENT_PLAYER_HAS_TECHNOLOGY"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_APPRENTICESHIP",
		"TechnologyType",
		"TECH_APPRENTICESHIP"
	);
	```
