---
tags:
- RequirementType
title: REQUIREMENT_TEAM_HAS_MOST_WMD_CITY_HITS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_TEAM_HAS_MOST_WMD_CITY_HITS
>
> * Class: `TEAMS`
> * Arguments:
>	* MinHitsRequired `Unknown`

## Samples

```SQL {title="ARMAGEDDON_VICTORY_REQUIRES_TEAM_HAS_MOST_WMD_DIRECT_CITY_HITS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"ARMAGEDDON_VICTORY_REQUIRES_TEAM_HAS_MOST_WMD_DIRECT_CITY_HITS",
		"REQUIREMENT_TEAM_HAS_MOST_WMD_CITY_HITS"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"ARMAGEDDON_VICTORY_REQUIRES_TEAM_HAS_MOST_WMD_DIRECT_CITY_HITS",
		"MinHitsRequired",
		1
	);
	
```
