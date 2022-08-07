---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_OPTIMUS_PRINCEPS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_OPTIMUS_PRINCEPS
>
> * Class: `PLAYERS`
> * Parameters:
>	* BetterTerritoryBonus `Integer`
>	* HiddenAgenda `Boolean`
>	* SimpleModifierDescription `String`
>	* StatementKey `String`
>	* TopTerritoryBonus `Integer`

## Samples

```SQL {title="AGENDA_EXPANSIONIST"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_EXPANSIONIST",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_OPTIMUS_PRINCEPS",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_30_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_EXPANSIONIST",
		"BetterTerritoryBonus",
		4
	),
	(
		"AGENDA_EXPANSIONIST",
		"HiddenAgenda",
		1
	),
	(
		"AGENDA_EXPANSIONIST",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_DESCRIPTION_EXPANSIONIST"
	),
	(
		"AGENDA_EXPANSIONIST",
		"StatementKey",
		"AGENDA_EXPANSIONIST_WARNING"
	),
	(
		"AGENDA_EXPANSIONIST",
		"TopTerritoryBonus",
		6
	);
	
```


```SQL {title="AGENDA_OPTIMUS_PRINCEPS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_OPTIMUS_PRINCEPS",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_OPTIMUS_PRINCEPS",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_10_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_OPTIMUS_PRINCEPS",
		"StatementKey",
		"AGENDA_OPTIMUS_PRINCEPS_WARNING"
	);
	
```

